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
my $mail;


print $q->header();

$user = $q->param('user');
$pass = $q->param('pass');
$pass2 = $q->param('pass2');
$name = $q->param('name');
$surname = $q->param('surname');
$Email = $q->param('Email');
$mail = $q->param('mail');

my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',-login=>'AdAdRoLu@gmail.com',-pass=>'Admin1212');

print "session error: $error" unless ($email!=-1);
 
$mail->send(-to=>'hugo1603@usal.es', -subject=>'Intento de conexion', -body=>'Just testing it');
 
$mail->bye;


print "Location: /altacorrecta.html\n\n";
