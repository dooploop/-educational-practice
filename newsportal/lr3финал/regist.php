<?php 
include 'header.php';
include 'function.php';

session_start();


//unset($_SESSION['user']);
	# code...
//if(!isset($_POST['confirm'])){
echo '<form action="regist.php" method="post">';
	echo '<div>';
		echo '<label for="name">Введите данные для регистрации </label> <br>';
		echo '<div>Логин</div>';
		echo '<input type="text" name="login" id="login" value="" tabindex="1" /> <br>';
		echo '<div>Пароль</div>';
		echo '<input type="password" name="passw" id="paw" value="" tabindex="1" autocomplete="new-password"/> <br>';
		echo '<div>Псевдоним</div>';
		echo '<input type="text" name="username" id="uname" value="" tabindex="1" /> <br>';

	echo '</div>';

	echo '<div>';
		echo '<input name="confirm" type="submit" value="Submit"/>';
	echo '</div>';
echo '</form>';

//$_post['login'];
//$user = array('login' => $ ,'pw' => $,'username' => $);

if(isset($_POST['confirm'])){
	$login = $_POST['login'];
	//$login = trim(filter_var($_POST['login'], FILTER_SANITIZE_STRING));
	$passw = $_POST['passw'];
	if (empty($_POST['username'])) {
		$username = $login;
	}
	else $username=$_POST['username'];// $username = trim(filter_var($_POST['username'], FILTER_SANITIZE_STRING));
	$nu[] = $login;
	$nu[] = $passw;
	$nu[] = $username;
	$nu[] = mt_rand();
	$user[]=$nu;

	output_users($user);


	if ((!empty($login)) and (!empty($passw))) {
			//echo "Регистрации прошла успешно,войдите в аккаунт";
			echo '<a href="auth.php"> Войти в аккаунт</a>';

	//$_SESSION['user'] = $user;
		}

}else echo 'Введи все данные';
 ?>
