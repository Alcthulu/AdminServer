#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use File::Copy::Recursive qw(dircopy);

my $q = CGI->new;
print $q->header();


my $user = $q->param('user');
my $ruta = "/var/html/wp".$user;

mkdir $ruta;

my $origen = "/var/configuracion/wordpress";
my $destino = "/var/www/html/wp".$user;

dircopy($origen, $destino);