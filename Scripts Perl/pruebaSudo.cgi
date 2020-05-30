#!/usr/bin/perl -w
use strict;
use warnings;

use CGI;
use Sudo;
my $su;

my $name='script_user';
my $pass='1234';

 
$su = Sudo->new(
                {
                 sudo         => '/usr/bin/sudo',
                 sudo_args    => '',                                  
                 username     => $name, 
                 password     => $pass,
                 program      => '/usr/lib/cgi-bin/2/pruebaAddUser.pl',
                 program_args => 'pepe, pepe12, 1003',
                # and for remote execution ...
 
                [hostname     => 'remote_hostname',]
                [username     => 'remote_username']
 
                }
               );
  
$result = $su->sudo_run();
if (exists($result->{error})) 
   { 
     &handle_error($result); 
   }
  else
   {
     printf "STDOUT: %s\n",$result->{stdout};
     printf "STDERR: %s\n",$result->{stderr};
     printf "return: %s\n",$result->{rc};
   }