#!/usr/bin/perl

use strict;
use warnings;

use File::Path;

my $user=$ARGV[0];


my $borrar = "/var/www/html/wp".$user;

rmtree($borrar, 1, 1);
