<?php 
//uset($_POST);
session_start();
//unset($_SESSION['user']);
include 'header.php';
function input_users()
	{
		$file = fopen('users.csv', 'r');
		$users = array();
		while (!feof($file))
		{
			$a = fgetcsv($file,1000,';');
			if ($a[0] !== NULL)
			{
				$users[] = $a;
			}
		}
		fclose($file);
		$_SESSION['users'] = $users;
	}

input_users();
$users = $_SESSION['users'];
//print_r($users);

//print_r($_SESSION['users']);
//unset($_SESSION['user']);
//include 'header.php';
if(!isset($_SESSION['user'])){
echo '<h4>Заполните данные:</h4>';
echo '<form action="auth.php" method="POST">';
	echo '<div>';
		//echo '<label for="name">Введите данные для регистрации </label> <br>';
	echo '<label for="login">Логин</label>';
		echo '<input type="text" name="login" id="login" value="" tabindex="1" /> <br>';
	echo '<label for="paw">Пароль</label>';

		echo '<input type="text" name="passw" id="paw" value="" tabindex="1" /> <br>';

	echo '</div>';

	echo '<div>';
		echo '<input name="confirm" type="submit" value="Submit"/>';
	echo '</div>';
echo '</form>';
}
else if(isset($_SESSION['user'])){
	echo "Пользователь авторизован";
	echo '<form action="auth.php" method="POST">';
		echo '<input name="exit" type="submit" value="Выйти"/>';

		if (isset($_POST['exit'])) {
			unset($_SESSION['user']);
 			echo "<meta http-equiv = 'refresh' content = '0'>";

		}
	echo '</form>';


}

	$login = trim(filter_var($_POST['login'], FILTER_SANITIZE_STRING));
	$passw = $_POST['passw'];
	//$user = array($login,$passw );
	//echo $login;
	//echo $passw;
foreach ($users as $value) {
	if (isset($_POST['confirm'])) {
	//	echo "sa";
		//print_r($value);
		if ($value[0] == $login and $value[1]==$passw) {
		$username = $value[2];
		$id = $value[3];
		$status = $value[4];
		$user = array($login,$passw,$username,$id,$status);
		$_SESSION['user'] = $user;
		$username = $value[2];
 		echo "<meta http-equiv = 'refresh' content = '0'>";
		}
 		//echo "<meta http-equiv = 'refresh' content = '0'>";
 		else if($value[0]==$login and $value[1]!=$passw ){

			echo "Пароль неверный";
			break;
			
		}else if($value[0]!=$login and $value[1]==$passw ){
			echo "Логин неверный";
			break;
		}else if (empty($login) or empty($passw)) {
			echo 'Заполните все поля';
			break;
		}
		else{
			continue ;
		}
	}
}

