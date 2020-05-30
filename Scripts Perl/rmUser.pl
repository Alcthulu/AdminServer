#!/usr/bin/perl

use strict;
use warnings;

use Linux::usermod;
use File::Path;

my $username;

my $user = Linux::usermod->del($username);

my $home="/home/".$user."/";
rmtree($home, 1, 1);
