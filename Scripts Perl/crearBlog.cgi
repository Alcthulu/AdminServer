#!/usr/bin/perl

use strict;
use warnings;

use CGI;

my $q = CGI->new;
print $q->header();


my $user = $q->param('user');
my $ruta = "/var/html/wp".$user;

print $user;

#mkdir $ruta;