#!/usr/bin/perl -w
use strict;
use warnings;

use CGI;
use Linux::usermod;
use Quota;
use File::chown;
use File::Copy::Recursive qw(dircopy);



my $user = $ARGV[0];
my $pass = $ARGV[1];
my $group = $ARGV[2];
my $home="/home/".$user;
my $shell="/bin/bash";

mkdir $home;

Linux::usermod->add($user, $pass, '', $group, '', $home, $shell);

my $userr=Linux::usermod->new($user);
my $uiduser=$userr->get(2);

dircopy("/etc/skel", $home);

chown $uiduser, $group, $home;
chmod (0700, $home);




#CUOTAS
my $dev=Quota::getqcarg();
my $tammax=80000;

Quota::setqlim($dev,$uiduser,$tammax,$tammax,0,0);
Quota::sync($dev);
