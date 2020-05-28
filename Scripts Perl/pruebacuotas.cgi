#!/usr/bin/perl
use strict;
use warnings;

use Quota;
use Linux::usermod;

my $username = 'juanito';
my $pass = '1234';
my $gid = 1004;
my $home="/home/".$username;
my $shell="/bin/bash";
my $tammax=70000;

mkdir $home;




Linux::usermod->add($username, $pass, '', $gid, '', $home, $shell) or die "Error al crear el usuario";

my $user=Linux::usermod->new($username);
my $uid = $user->get(2);

chown $uid, $gid, $home;

print("Creado el usuario ".$username."con uid".$uid);

my $dev=Quota::getqcarg();

Quota::setqlim($dev,$uid,$tammax,$tammax,0,0);
Quota::sync($dev);