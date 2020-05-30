#!/usr/bin/perl -w
use strict;
use warnings;

use CGI;
use Linux::usermod;



my $user = $ARGV[0];
my $pass = $ARGV[1];
my $group = $ARGV[2];
my $home="/home/".$user;
my $shell="/bin/bash";

Linux::usermod->add($user, $pass, '', $group, '', $home, $shell);
