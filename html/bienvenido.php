<!DOCTYPE php>
<html lang="es">
	<head>
		<meta charset="UTF-8">
		<title>Bienvenido</title>
		<link rel="stylesheet" href="css/SignUpStyle.css">
	</head>

		<div class="topBar">
		    <header id="logo">
		        AdRoLu/moodle
		    </header>
		    <a href="Bienvenido.php" class="headNav">Página principal</a>
		    <a href="modificar.php" class="headNav">Modificar perfil</a>
		    <a href="" class="headNav">Blog personal</a>"
		    <a href="roundcube" class="headNav">Correo electrónico</a>
		    <?php
		      	session_start();
		        if(isset($_SESSION["LoggedIn"]) && $_SESSION["LoggedIn"] == true){
		          echo "<a href=\"LogOut.php\" id=\"LogoutButton\">Logout</a>";
		        }else{
		          echo "<a href=\"LoginPage.php\" id=\"LoginButton\">Login</a>";
		        }
		    ?>
		</div>
	<body>
		<br>
		<ul>
		<p>Para darte de alta pulse <a href="https://142.93.43.11/signup.html">aquí</a></p>
		<p>Para darte de baja pulse <a href="https://142.93.43.11/baja.html">aquí</a></p>
		<p>Para modificar tus datos pulse <a href="https://142.93.43.11/modificar.html">aquí</a></p>
		<p>Para iniciar sesión pulse <a href="https://142.93.43.11/login.html">aquí</a></p>
		</ul>
	</body>
</html>