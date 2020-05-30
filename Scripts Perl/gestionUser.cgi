#!/usr/bin/perl

use strict;
use warnings;

use DBI;
use CGI;

my $username;
my $idAccion;
my $contrasena;



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

		my $encrypt = Digest::MD5->new;
        my $enpass = $encrypt->md5_base64($contrasena);

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

        }


		$consulta->finish();
		$conexion->disconnect();
	}

	case "modifica" {

	}
};