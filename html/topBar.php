
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" href="/resources/demos/style.css">
    <div class="topBar">
      <header id="logo">
        AdRoLu/moodle
      </header>
      <a href="Home.php" class="headNav">Página principal</a>
      <a href="Genres.php" class="headNav">Modificar perfil</a>
      <a href="Platforms.php" class="headNav">Blog personal</a>
      <?php
        session_start();
        if(isset($_SESSION["LoggedIn"]) && $_SESSION["LoggedIn"] == true){
          echo "<a href=\"LogOut.php\" id=\"LogoutButton\">Logout</a>";
        }else{
          echo "<a href=\"LoginPage.php\" id=\"LoginButton\">Login</a>";
        }
      ?>
    </div>