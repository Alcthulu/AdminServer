#!/usr/bin/perl -w
use strict;
use warnings;

use Passwd::Unix;

my $user = $ARGV[0];
my $pass = $ARGV[1];

my $pw = Passwd::Unix->new();
$pw->passwd($user, $pw->encpass($pass));
