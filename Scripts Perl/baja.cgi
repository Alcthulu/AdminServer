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
my $contrasena=$q->param('contrasena');

my $consul= "SELECT *FROM personitas where user='$username'";

my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
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
	$conexion->do("DELETE FROM personitas WHERE user='$username'");

	my $su;
	my $namer='root';
	my $passr='Admin12';
	my $result='';
	my $params="$username";

	$su = Sudo->new(
	                {
	                 sudo         => '/usr/bin/sudo',
	                 sudo_args    => '',                                  
	                 username     => $namer,
	                 password     => $passr,
	                 program      => '/usr/lib/cgi-bin/2/rmUser.pl',
	                 program_args => $params,
	                  # and for remote execution ...
	   
	  #                [hostname     => 'remote_hostname',]
	  #                [username     => 'remote_username']
	   
	                }
	               );
	    
	$result = $su->sudo_run();


	if (exists($result->{error})) 
	{ 
	    &handle_error($result); 
	}


	$consulta->finish();
	$conexion->disconnect();
	print "Usuario eliminado";
    print "<meta http-equiv='refresh' content='3; https://142.93.43.11/LogOut.php'>";
}else {
	  print qq[<html><head><p>Contraseña incorrecta, <a href="https://142.93.43.11/modificar.php">vuelva</a> a intentarlo.</p></head></html>];
};
