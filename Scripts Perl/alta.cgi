#!/usr/bin/perl
use strict;
use warnings;

use CGI;

my $q = CGI->new;

my $nombre = $q->param("nombre");
my $password = $q->param("password");

print "Location: /altacorrecta.html\n\n";
