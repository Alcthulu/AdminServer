#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use Email::Send::SMTP::Gmail;
use Linux::usermod;
use Quota;


my $user;
my $pass;
my $pass2;
my $name;
my $surname;
my $Email;
my $correopostal;
my $gid;
my $home;
my $shell;

print $q->header();

$user = $ARGV[0];
$pass = $ARGV[1];
$pass2 = $ARGV[2];
$name = $ARGV[3];
$surname = $ARGV[4];
$Email = $ARGV[5];
$correopostal = $ARGV[6];
if($ARGV[7]) eq "Profesor"){
	$gid=1003;
}else{
	$gid=1004;
};
$home="/home/".$user;
$shell="/bin/bash";
#$shell="/bin/false";

my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","root","Admin12",{'RaiseError' => 1});


#Creamos el directorio para el usuario
mkdir $home;
#copiar condiciones.txt al directorio

#Damos de alta usuario en el sistema
Linux::usermod->add($user, $pass, '', $gid, '', $home, $shell) or die "Error al crear el usuario";

#userr es un objeto que representa al usuario
my $userr=Linux::usermod->new($user);
my $uiduser=$userr->get(2);

chown $uiduser, $gid, $home;

print ("El usuario $user hace login con la contrasena $pass");


#Dar permisos de ejecución: chmod u+x alta.cgi



my $dev=Quota::getqcarg();
my $tammax=80000;

Quota::setqlim($dev,$uiduser,$tammax,$tammax,0,0);
Quota::sync($dev);