<!DOCTYPE php>
<html lang="es">
	<head>
		<meta charset="UTF-8">
		<title>Bienvenido</title>
		<link rel="stylesheet" href="css/SignUpStyle.css">
	</head>

		<div class="topBar">
		    
		    <a>AdRoLu/moodle</a>
		    <a href="https://142.93.43.11/bienvenido.php" class="headNav">Página principal</a>
		    <a href="https://142.93.43.11/modificar.php" class="headNav">Modificar perfil</a>
		    <a href="" class="headNav">Blog personal</a>
		    <a href="https://142.93.43.11/roundcube" class="headNav">Correo electrónico</a>
		    <?php
		      	session_start();
		        if(isset($_SESSION["LoggedIn"]) && $_SESSION["LoggedIn"] == true){
		          echo "<a href=\"https://142.93.43.11/LogOut.php\" id=\"LogoutButton\">Logout</a>";
		        }else{
		          echo "<a href=\"https://142.93.43.11/login.php\" id=\"LoginButton\">Login</a>";
		        }
		    ?>
		</div>
	<body>
		<br>
		<div>
			<p>Para darte de alta dirijase a la sección de login y presione el enlace de ¿No tienes cuenta?.</p>
		</div>
		<div>
			<p>Para darte de baja pulse , una vez identificado con su usuario, dirijase a la sección Modificar perfil y elija la opción eliminar cuenta.</p>
		</div>
		<div>
			<p>Para modificar su perfil, una vez identificado con su usuario, dirijase a la sección Modificar perfil y elija la opción deseada.</p>
		</div>
		<div>
			<p>Para iniciar sesión dirijase a la sección login en la parte superior de la pantalla en caso de no estar identificado.</p>
		</div>
	</body>
</html>