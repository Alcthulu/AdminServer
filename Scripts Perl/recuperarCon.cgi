#!/usr/bin/perl

use strict;
use warnings;

use DBI;
use CGI;
use Digest::MD5 qw(md5_base64);
use Sudo;


my $q = CGI->new;

print $q->header();

my $username=$q->param('user');
my $pass=$q->param('pass');
my $pass2=$q->param('pass2');
my $clave=$q->param('token');

my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
my $consul = "SELECT *FROM personitas where user='$username'";
my $consulta = $conexion->prepare($consul);
$consulta->execute();

my $datos;
my @data;
my $token;

while($datos = $consulta->fetchrow_arrayref())
{
  push @data, @$datos;
  
  $token= $data[8];
}

if($clave eq $token){
	if($pass eq $pass2){
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
		my $enpass = md5_base64($pass);
		$conexion->do("UPDATE personitas SET pass='$enpass' where user='$username'");
	}else{
		print qq[<html><head><p>Las contrasñas no coinciden,<a href="https://142.93.43.11/recuperarCon.html">vuelva</a> a intentarlo.</p></head></html>];

	}
}else{
	print qq[<html><head><p>Clave incorrecta, <a href="https://142.93.43.11/recuperarCon.html">vuelva</a> a intentarlo.</p></head></html>];
}

$consulta->finish();
$conexion->disconnect();