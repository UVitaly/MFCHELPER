<?php
 $email = filter_var(trim($_POST['email']),FILTER_SANITIZE_STRING);
 $password = filter_var(trim($_POST['pass']),FILTER_SANITIZE_STRING);

 $mysql = new mysqli('localhost','root','','pract');
 mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

 $password = md5($password."glhfalrd34");

 $query = $mysql->query("SELECT * FROM `users` WHERE `email` = '$email' AND `pass` = '$password'");
 $user = $query->fetch_assoc();

if(count($user) == 0)
{
	echo "Такого пользователя не существует";
	exit();
}
session_start();

setcookie('user', $user['name'], time() + 14800, "/");
setcookie('work', $user['posts_name'], time() + 14800, "/");


if($user['admin']==1)
{
	$mysql->close();
	header('Location: /admin.php');
	exit();
}
$mysql->close();
header('Location: /index.php');

exit();
?>