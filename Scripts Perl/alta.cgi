#!/usr/bin/perl
use strict;
use warnings;

use CGI;

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


print "Location: /altacorrecta.html\n\n";
