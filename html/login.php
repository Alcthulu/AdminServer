<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Inicio de sesión</title>
  <link rel="stylesheet" href="css/LoginPageStyle.css">
</head>
  <body>
    <a href="https://142.93.43.11/bienvenido.php" id="cancel">Cancelar</a>
    <form class="fromularioLogin" action="Verify.php" method="post">
      <label for="user"><b>Nombre de usuario</b></label>
      <input type="text" placeholder="Nombre de usuario" name="user" id="user" required>

      <label for="pass"><b>Contraseña</b></label>
      <input type="password" placeholder="Contraseña" name="pass" id="pass" required>

      <button type="submit">Aceptar</button>
      <a href="https://142.93.43.11/signup.html" id="SignUpLink">¿No tienes cuenta?</a>
      <a href="https://142.93.43.11/correoRecuperacion.html" id="RecuLink">¿No recuerdas tu contraseña?</a>
    </form>
  </body>
</html>