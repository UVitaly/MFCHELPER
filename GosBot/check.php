<?php
$login = filter_var(trim($_POST['login']),FILTER_SANITIZE_STRING);
$name = filter_var(trim($_POST['name']),FILTER_SANITIZE_STRING);
$password = filter_var(trim($_POST['pass']),FILTER_SANITIZE_STRING);
$email = filter_var(trim($_POST['email']),FILTER_SANITIZE_STRING);
$ln = filter_var(trim($_POST['last_name']),FILTER_SANITIZE_STRING);
$mn = filter_var(trim($_POST['middle_name']),FILTER_SANITIZE_STRING);
$pn = filter_var(trim($_POST['posts_name']),FILTER_SANITIZE_STRING);

$mysql = new mysqli('localhost', 'root', '', 'pract');

if (mb_strlen($login)>30)
  {
  echo "Недопустимая длина логина";
  exit;
  }
  
  else if (mb_strlen($name)>30)
  {
  echo "Недопустимая длина имени";
  exit;
  }
  else if (mb_strlen($ln)>30)
  {
  echo "Недопустимая длина фамилии";
  exit;
  }
  else if (mb_strlen($mn)>30)
  {
  echo "Недопустимая длина отчества";
  exit;
  }
  else if (mb_strlen($password)<4 || mb_strlen($password)>15)
  {
  echo "Недопустимая длина пароля(от 4 до 15 символов)";
  exit;
  }

    $password = md5($password."glhfalrd34");

    
$mysql->query("INSERT INTO `users` ( `login`,`last_name`,`middle_name`,`posts_name`,`pass`, `name`, `email`)
VALUES('$login','$ln','$mn','$pn','$password', '$name', '$email')");

$mysql->close();
header('Location: /index.php');
?>

