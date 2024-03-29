#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use Sudo;
use DBI;

my $q = CGI->new;
print $q->header();

my $user = $q->param('user');

my $todrop="wp_".$user."commentmeta,  wp_".$user."comments,  wp_".$user."links,  wp_".$user."options,  wp_".$user."postmeta,  wp_".$user."posts,  wp_".$user."termmeta,  wp_".$user."terms,  wp_".$user."term_relationships,  wp_".$user."term_taxonomy,  wp_".$user."usermeta,  wp_".$user."users";
my $dropCon="DROP TABLE IF EXISTS ".$todrop;

my $conexion = DBI->connect("DBI:mysql:database=wordpressdb;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
my $consulta = $conexion->prepare($dropCon);
$consulta->execute();

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
  print "<meta http-equiv='refresh' content='3; https://142.93.43.11/bienvenido.php'>";
}

$consulta->finish();
$conexion->disconnect();

