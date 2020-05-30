#!/usr/bin/perl

use strict;
use warnings;

use DBI;
use CGI;
use Digest::MD5 qw(md5_base64);
use Sudo;
use Switch;

my $q = CGI->new;

print $q->header();

my $username=$q->param('user');;
my $idAccion=$q->param('id');;
my $contrasena=$q->param('pass');;



switch ($idAccion) {

	case "baja"{
		my $conexion = DBI->connect("DBI:mysql:database=soirausu;host=localhost","phpmyadmin","Admin12",{'RaiseError' => 1});
		my $consul = "SELECT *FROM personitas where user='$username'";
		my $consulta = $conexion->prepare($consul);
		$consulta->execute();

		my $datos;
		my @data;
		my $password;

		while($datos = $consulta->fetchrow_arrayref())
		{
		  push @data, @$datos;
		  
		  $password= $data[1];
		}

        my $enpass = md5_base64($contrasena);

        if ($enpass eq $password) {
        	$conexion->do("DELETE FROM personitas WHERE user='$username'");

			my $su;
			my $name='root';
			my $pass='Admin12';
			my $result='';
			my $params="$username";

			$su = Sudo->new(
			                {
			                 sudo         => '/usr/bin/sudo',
			                 sudo_args    => '',                                  
			                 username     => $name,
			                 password     => $pass,
			                 program      => '/usr/lib/cgi-bin/2/rmUser.pl',
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
        }
        else {
        	  print qq[<html><head><p>Su cuenta ya ha sido activada, siga el siguiente <a href="https://142.93.43.11/login.html">enlace</a> para iniciar secion.</p></head></html>];
        	  print $enpass;
        	  print "\n";
        	  print $password;
        }


		$consulta->finish();
		$conexion->disconnect();
	}

	case "modifica" {

	}
};