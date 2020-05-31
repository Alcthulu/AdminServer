<!DOCTYPE php>
<html lang="es">
	<head>
		<meta charset="UTF-8">
		<title>Bienvenido</title>
		<link rel="stylesheet" href="css/ModStyle.css">

	</head>
	<?php
		session_start();
        if(isset($_SESSION["LoggedIn"]) && $_SESSION["LoggedIn"] == true){
			echo"
			<div class='topBar'>
		      <a>AdRoLu/moodle</a>
		      <a href='bienvenido.php' class='headNav'>Página principal</a>
		      <a href='modificar.php' class='headNav'>Modificar perfil</a>
		      <a href='' class='headNav'>Blog personal</a>
		      <a href='roundcube' class='headNav'>Correo electrónico</a>
		      <a href='LogOut.php' id='LogoutButton'>Cerrar sesion</a>
		   	</div>
			<body>
				<form class='formularioMod' action='/modificar.php' method='POST'>
				<br>
				<ul>

				<div><a href='modificarDatos.php' class='button'>Modificar Datos de usuario</a></div>
				<div><a href='/cgi-bin/crearBlog.cgi?user=".$_SESSION["User"]."' class='button'>-----Crear web personal-----</a></div>
				<div><a href='' class='button'>---Eliminar web personal---</a></div>
				<div><a href='baja.php' class='button'>-------Eliminar cuenta-------</a></div>
				</ul>
			</form>
			</body>
			";
		}
        else{
          header("location:https://142.93.43.11/login.php");
        }
    ?>
</html>