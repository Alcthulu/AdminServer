<?php 
  $Username = $_POST["user"];
  $password = $_POST['pass']; 

  $mysqli = mysqli_connect("localhost", "phpmyadmin", "Admin12", "soirausu");
  if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: ".mysqli_connect_error();
  
  }

  function md5_base64( $data ) {
    return preg_replace('/=+$/','',base64_encode(pack('H*',md5($data))));
  }

  $enpass = md5_base64($password);

  $res = mysqli_query($mysqli, "SELECT user, pass  FROM personitas WHERE user = '$Username' AND  pass = '$enpass'");
  if(!$res) {
    print("MySQL error: " . mysqli_error($mysqli));
    exit;
  }  

  $rows = mysqli_num_rows($res);
  if($rows == 1){
    session_start();
    $_SESSION["User"] = $Username;
    $_SESSION["LoggedIn"] = true;
    header("location:modificarDatos.php");
  }else{
    $_SESSION["LoggedIn"] = false;
    header("location:login.php?error=login");
  }
  mysqli_free_result($res);
  mysqli_close($mysqli);
?>
  