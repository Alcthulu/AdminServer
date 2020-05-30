#!/usr/bin/perl

use strict;
use warnings;

use DBI;
use CGI;
use Digest::MD5 qw(md5_base64);
use Sudo;
use Switch;

my $q = CGI->new;

print $q->header();

my $username=$q->param('user');
my $contrasena=$q->param('contrasena');
my $pass=$q->param('pass');
my $pass2=$q->param('pass2');
my $name=$q->param('name');
my $surname=$q->param('surname');
my $email=$q->param('Email');
my $correopostal=$q->param('correopostal');

my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
my $consul = "SELECT *FROM personitas where user='$username'";
my $consulta = $conexion->prepare($consul);
$consulta->execute();

my $datos;
my @data;
my $password;

while($datos = $consulta->fetchrow_arrayref())
{
  push @data, @$datos;
  
  $password= $data[1];
}

my $enpass = md5_base64($contrasena);

if ($enpass eq $password) {

	if(($pass ne undef) && ($pass2 ne undef) && ($pass eq $pass2))
		{
		my $su;
		my $namer='root';
		my $passr='Admin12';
		my $result='';
		my $params="$username $pass";

		$su = Sudo->new(
		                {
		                 sudo         => '/usr/bin/sudo',
		                 sudo_args    => '',                                  
		                 username     => $namer,
		                 password     => $passr,
		                 program      => '/usr/lib/cgi-bin/2/chgPass.pl',
		                 program_args => $params,
		   
		                }
		               );
		    
		$result = $su->sudo_run();


		if (exists($result->{error})) 
		{ 
		    &handle_error($result); 
		}
		$enpass = md5_base64($pass);
		$conexion->do("UPDATE personitas SET pass='$enpass' where user='$username'");

		if($name ne undef)
		{
			$conexion->do("UPDATE personitas SET name='$name' where user='$username'");

		}

		if($surname ne undef)
		{
			$conexion->do("UPDATE personitas SET surname='$surname' where user='$username'");

		}

		if($email ne undef)
		{
			$conexion->do("UPDATE personitas SET email='$email' where user='$username'");
		}
		
		if($correopostal ne undef)
		{
			$conexion->do("UPDATE personitas SET correopostal='$correopostal' where user='$username'");
		}


	}
	else {
		if($name ne undef)
		{
			$conexion->do("UPDATE personitas SET name='$name' where user='$username'");

		}

		if($surname ne undef)
		{
			$conexion->do("UPDATE personitas SET surname='$surname' where user='$username'");

		}

		if($email ne undef)
		{
			$conexion->do("UPDATE personitas SET email='$email' where user='$username'");
		}
		
		if($correopostal ne undef)
		{
			$conexion->do("UPDATE personitas SET correopostal='$correopostal' where user='$username'");
		}
	}
}

$consulta->finish();
$conexion->disconnect();