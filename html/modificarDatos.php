<!DOCTYPE php>
<html>
	<head>
		<meta charset="UTF-8">		
		<title>Formulario de modificaciones</title>
		<link rel="stylesheet" href="css/ModDatStyle.css">		
	</head>
	<body>
	<?php
		session_start();
        if(isset($_SESSION["LoggedIn"]) && $_SESSION["LoggedIn"] == true){
			echo"
			<div class='topBar'>
		      <a>AdRoLu/moodle</a>
		      <a href='https://142.93.43.11/bienvenido.php' class='headNav'>Página principal</a>
		      <a href='https://142.93.43.11/modificar.php' class='headNav'>Modificar perfil</a>
		      <a href='wp".$_SESSION["User"]."' class='headNav'>Blog personal</a>
		      <a href='https://142.93.43.11/roundcube' class='headNav'>Correo electrónico</a>
		      <a href='https://142.93.43.11/LogOut.php' id='LogoutButton'>Cerrar sesion</a>
		   	</div>

			<div class='Display'>
				<form class='formularioModDat' action='/cgi-bin/modificaDatos.cgi' method='POST'>

				    <br><br><br><br>
					Rellena solo los campos de los datos que quieras modificar:
					<br><br>

		    		<label for='name'><b>Nuevo nombre</b></label>
		    		<input type='text' placeholder='Nombre' name='name' id='name' >

		    		<label for='surname'><b>Nuevos apellidos</b></label>
		    		<input type='text' placeholder='Apellidos' name='surname' id='surname' >

		  			<label for='pass'><b>Nueva contraseña</b></label>
		    		<input type='password' placeholder='Contraseña' name='pass' id='pass' >

		    		 <label for='pass2'><b>Repita la nueva contraseña</b></label>
		    		<input type='password' placeholder='Contraseña' name='pass2' id='pass2' >

		    		<label for='Email'><b>Nuevo correo electrónico</b></label>
		    		<input type='email' placeholder='Correo electrónico' name='Email' id='Email' >

					<label for='mail'><b>Nuevo correo postal</b></label>
		    		<input type='text' placeholder='Correo postal' name='correopostal' id='correopostal' >

		    		<p>--------------------------------------------------------------------</p>
					<label for='user'><b>Nombre de usuario</b></label>
		    		<input type='text' placeholder='User' name='user' id='user' required>

		    		<label for='contrasena'><b>Contraseña actual</b></label>
		    		<input type='password' placeholder='Contraseña' name='contrasena' id='contrasena' required>

					<button type='submit'>Enviar</button>
					<br><a href='https://142.93.43.11/modificar.html'>Volver</a>

				</form>
			</div>";
		}
        else{
          header("location:https://142.93.43.11/login.php");
        }
    ?>
	</body>
</html>