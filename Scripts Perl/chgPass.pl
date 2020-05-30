#!/usr/bin/perl -w
use strict;
use warnings;

use Unix::Passwd:File;

my $user = $ARGV[0];
my $pass = $ARGV[1];

my $res = list_users();

$res = modify_user(user=>"$user", pass=>"$pass");