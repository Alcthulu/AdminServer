#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use Sudo;
use DBI;
use Digest::MD5 qw(md5_base64);

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

my $conf;

while($datos = $consulta->fetchrow_arrayref())
{
  push @data, @$datos;
  
  $password= $data[1];
  $group = $data[6];
  $conf = $data[7];
}

if ($conf == 1){
  
  print qq[<html><head><p>Su cuenta ya ha sido activada, siga el siguiente <a href="https://142.93.43.11/login.html">enlace</a> para iniciar secion.</p></head></html>];

}else{
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
                   program      => '/usr/lib/cgi-bin/2/addUser.pl',
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

        print qq[<html><head><p>Se ha dado de alta correctamente, para acceder a su cuenta pulse  <a href="https://142.93.43.11/login.html">aqui</a>.</p></head></html>];
        

        my $enpass = md5_base64($password);

        my $conexion= DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
        my $consulta = $conexion->prepare("UPDATE personitas SET confirmado=1 WHERE user='$username'");
        $consulta->execute();
        $conexion->do("UPDATE personitas SET pass='$enpass' WHERE user='$username'");
        $consulta->finish();
        $conexion->disconnect();
     }
}


