#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use Sudo;

my $q = CGI->new;
print $q->header();

my $user = $q->param('user');

my $su;
my $namer='root';
my $passr='Admin12';
my $result='';
my $params="$user";

$su = Sudo->new(
                {
                 sudo         => '/usr/bin/sudo',
                 sudo_args    => '',                                  
                 username     => $namer,
                 password     => $passr,
                 program      => '/usr/lib/cgi-bin/2/eliminarBlog.pl',
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
}else{
    print "Blog eliminado";
    print "<meta http-equiv='refresh' content='3; ../wp".$user."'>";
}


