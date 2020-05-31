#!/usr/bin/perl

use strict;
use warnings;

use File::Copy::Recursive qw(dircopy);
use Tie::File;



my $user = $ARGV[0];
my $ruta = "/var/html/wp".$user;

mkdir $ruta;

my $origen = "/var/configuracion/wordpress";
my $destino = "/var/www/html/wp".$user;

dircopy($origen, $destino);

my $archivo = $destino."/wp-config.php";

my @contenido;

tie @contenido, 'Tie::File', $archivo or die "No se logró hacer el tie: $!";

my $newline = "\$table_prefix = 'wp_".$user."';";

$contenido[65] = $newline;

untie @contenido;



