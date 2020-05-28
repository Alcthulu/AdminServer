#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use Sudo;

my $q = CGI->new;

my $namee=www-data;
my $passw=;

my $user = $q->param('user');
my $pass = $q->param('pass');
my $pass2 = $q->param('pass2');
my $name = $q->param('name');
my $surname = $q->param('surname');
my $Email = $q->param('Email');
my $correopostal = $q->param('correopostal');
my $group = $q->param('group');


$su = Sudo->new(

                sudo => '/usr/bin/sudo',
                sudo_args => '',
                username => $namee,
                password => $passw,
                program => '/usr/lib/cgi-bin/2/alta.cgi',
                program_args => '$user, $pass, $pass2, $name, $surname, $Email, $correopostal, $group',
                #and for remote execution ...

                [hostname => 'remote_hostname',]
                [username => 'remote_username']

        }
);

$result = $su->sudo_run();
if(exists($result->{error}))
{
        &handle_error($result);
}
else
{
        printf "STDOUT: %s\n",$result->{stdout};
        printf "STDERR: %s\n",$result->{stderr};
        printf "return: %s\n",$result->{rc};
}