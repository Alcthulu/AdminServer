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


print $q->header();

$user = $q->param('user');
$pass = $q->param('pass');
$pass2 = $q->param('pass2');
$name = $q->param('name');
$surname = $q->param('surname');
$Email = $q->param('Email');
$correopostal = $q->param('correopostal');

my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',-login=>'AdAdRoLu@gmail.com',-pass=>'Admin1212');

print "session error: $error" unless ($mail!=-1);
 
$mail->send(-to=>'hugo1603@usal.es', -subject=>'Intento de conexion', -body=>'Just testing it');
 
$mail->bye;


print ("El usuario $user hace login con la contrasena $pass");
