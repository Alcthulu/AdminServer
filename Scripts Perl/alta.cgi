#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use Email::Send::SMTP::Gmail;

my $q = CGI->new;

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

$user = $q->param('user');
$pass = $q->param('pass');
$pass2 = $q->param('pass2');
$name = $q->param('name');
$surname = $q->param('surname');
$Email = $q->param('Email');
$correopostal = $q->param('correopostal');
if($q->param('group')==Profesor) gid=1003 else gid=1004;
$home="/home/".$user;
$shell="/bin/bash":
#$shell="/bin/false";


#Envio de correo desde adadrolu a hugo1603
my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',-login=>'AdAdRoLu@gmail.com',-pass=>'Admin1212');

print "session error: $error" unless ($mail!=-1);
 
$mail->send(-to=>'hugo1603@usal.es', -subject=>'Intento de conexion', -body=>'Just testing it');
 
$mail->bye;

#Creamos el directorio para el usuario
mkdir $home;
#copiar condiciones.txt al directorio
#Damos de alta usuario en el sistema
Linux::usermod->($user, $pass, '', $gid, '', $home, $shell);

chown $user $home;

print ("El usuario $user hace login con la contrasena $pass");
