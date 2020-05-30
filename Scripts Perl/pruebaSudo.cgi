#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use Sudo;

my $q = CGI->new;

print $q->header();

my $su;

my $name='root';
my $pass='Admin12';
my $result='';
my $username=$q->param('user');
my $password=$q->param('pass');
my $params="$username $password 1003";

$su = Sudo->new(
                {
                 sudo         => '/usr/bin/sudo',
                 sudo_args    => '',                                  
                 username     => $name,
                 password     => $pass,
                 program      => '/usr/lib/cgi-bin/2/pruebaAddUser.pl',
                 program_args => $params,
                # and for remote execution ...
 
#                [hostname     => 'remote_hostname',]
#                [username     => 'remote_username']
 
                }
               );
  
$result = $su->sudo_run();
if (exists($result->{error})) 
   { 
     &handle_error($result); 
   }
  else
   {
   }
