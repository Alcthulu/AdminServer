#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use Sudo;
use DBI;

my $q = CGI->new;

print $q->header();

my $username=$q->param('user');
my $token=$q->param('token');
my $password;
my $group;

my $consul= "SELECT *FROM personitas where user='$username' AND token='$token' ";


my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});

my $consulta = $conexion->prepare($consul);

$consulta->execute();

my $datos;
my @data;

while($datos = $consulta->fetchrow_arrayref())
{
  push @data, @$datos;
  
  $password= $data[1];
  $group = $data[6];
}

my $su;
my $name='root';
my $pass='Admin12';
my $result='';
my $params="$username $password $group";

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
