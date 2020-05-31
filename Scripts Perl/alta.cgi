#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use Sudo;
use DBI;
use Email::Send::SMTP::Gmail;

my $q = CGI->new;

print $q->header();


my $user = $q->param('user');
my $pass = $q->param('pass');
my $pass2 = $q->param('pass2');
my $name = $q->param('name');
my $surname = $q->param('surname');
my $Email = $q->param('Email');
my $correopostal = $q->param('correopostal');
my $group;
if($q->param('group') eq "Profesor"){
        $group=1003;
}else{
        $group=1004;
};
my $flag = 0;
my $confirmado = 0;

if($pass ne $pass2)
{
        $flag=1;
        print qq[<html><head><p>Las contraseñas no coinciden,  <a href="https://142.93.43.11/signup.html">intentelo de nuevo</a> asegurándose de que coincidan.</p></head></html>];      
}


my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
if($conexion == 1)
{
        $flag=1;
        print qq[<html><head></html>];     

}

my $datos;
my @usuarios;

my $consulta = $conexion->prepare("SELECT *FROM personitas where user = '$user'");
$consulta->execute();

while( $datos = $consulta->fetchrow_arrayref())
{
        push @usuarios, @$datos[0];
}
$consulta->finish();

if(scalar @usuarios > 0)
{
        $flag=1;
        print qq[<html><head><p>El nombre de usuario ya existe, pulse <a href="https://142.93.43.11/signup.html">aqui</a> para volver atrás.</p></head></html>];
}

my $consulta2 = $conexion->prepare("SELECT *FROM personitas where email = '$Email'");
$consulta2->execute();
while( $datos = $consulta2->fetchrow_arrayref())
{
        push @usuarios, @$datos[0];
}
$consulta2->finish();

if(scalar @usuarios > 0)
{
        $flag=1;
        print qq[<html><head><p>Este correo electrónico está en uso, pulse <a href="https://142.93.43.11/signup.html">aqui</a> para volver atrás.</p></head></html>];
}


if($flag == 0) {

        my $token = 1000000 + int(rand(9999999));
        my $mailbody = "Pulsa este enlace para confirmar https::/142.93.43.11/cgi-bin/confirmacion.cgi?user=$user&token=$token";

        my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',-login=>'AdAdRoLu@gmail.com',-pass=>'Admin1212');

        print "session error: $error" unless ($mail!=-1);
         
        $mail->send(-to=>'hugo1603@usal.es', -subject=>'Correo de confirmación', -body=> $mailbody);
         
        $mail->bye;

        $conexion->do("INSERT INTO personitas VALUES (?,?,?,?,?,?,?,?,?)",undef,$user,$pass,$name,$surname,$Email,$correopostal,$group,$confirmado,$token);

        print qq[<html><head><p>Se le ha enviado un enlace de confirmación a su correo electrónico, trás verificar su identidad en dicho enlace podrá acceder a su moodle <a href="https://142.93.43.11/login.php">aqui</a>.</p></head></html>];

}
$conexion->disconnect();


