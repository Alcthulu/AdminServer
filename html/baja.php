<!DOCTYPE php>
<html lang="es">
	<head>
		<meta charset="UTF-8">
		<title>Formulario de baja</title>
		<link rel="stylesheet" href="css/SignUpStyle.css">
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
				<form class='formularioAlta' action='/cgi-bin//baja.cgi' method='POST'>

				    <label for='user'><b>Nombre de usuario</b></label>
				    <input type='text' placeholder='Nombre de usuario' name='user' id='user' required>

				    <label for='pass'><b>Contraseña</b></label>
				    <input type='password' placeholder='Contraseña' name='contrasena' id='contrasena' required> 

					<button type='submit'>Dar de baja</button>
					<br><a href='/bienvenido.php'>Volver</a>

				</form>
			</body>";
		}
        else{
          header("location:https://142.93.43.11/login.php");
        }
    ?>
</html>