#!/usr/bin/perl

use strict;
use warnings;

use Email::Send::SMTP::Gmail;
use DBI;
use CGI;

my $q = CGI->new;
print $q->header();

my $Email = $q->param('Email');






my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});

my $consul = "SELECT *FROM personitas where email = '$Email'";
my $consulta = $conexion->prepare($consul);
$consulta->execute();

my $datos;
my @usuarios;
my $username;
my @data;

while( $datos = $consulta->fetchrow_arrayref())
{
    push @usuarios, @$datos[0];
    push @data, @$datos;
    $username = $data[0];
}
$consulta->finish();

if(scalar @usuarios > 0)
{
	$conexion->do("UPDATE personitas SET token='$token' where email='$Email'");        
}




my $token = 1000000 + int(rand(9999999));
my $mailbody = "Tu usuario es $username. Pulsa este enlace y recuerde esta clave $token para recuperar su contraseña https::/142.93.43.11/recuperarCon.html";

my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',-login=>'AdAdRoLu@gmail.com',-pass=>'Admin1212');

print "session error: $error" unless ($mail!=-1);
 
$mail->send(-to=>'hugo1603@usal.es', -subject=>'Correo de recuperacion de contraseña', -body=> $mailbody);
$mail->bye;
