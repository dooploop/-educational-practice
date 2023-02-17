<?php 


session_start();

//$users = array('user' => 'amir');
//$_SESSION['user'] = '3mir';
 //echo $_SESSION['user'][4];
echo '<!DOCTYPE html>';
echo '<html lang="en">';
echo '<head>';
	echo '<meta charset="UTF-8">';
	echo '<title>Статья</title>';
	echo '<link rel="stylesheet" href="style.css" media="screen" type="text/css">';
echo '</head>';
echo '<body>';
	echo '	<div class="header">';
	
		echo '<a href="index.php" class="logo">TheNewYorkTimes</a>';
		echo '<div class="header-right">';
	
	    echo '<a href="regist.php">Регистрация</a>';
	    echo '<a href="auth.php">Авторизация</a>';

  	echo '</div>';

echo '</div>';
echo '<div id = "menu_block">';

echo '	<form class = "lft" method="post" action="index.php">';
echo '	<input id = "menu_btn" type="submit" name="submitButton" value="Главная"/> </form>';
	
echo '	<form class = "lft" method="post" action="catalog.php">';
echo '	<input id = "menu_btn" type="submit" name="submitButton" value="Каталог"/> </form>';
if (isset($_SESSION['user'])) {
	echo '	<form class = "lft" method="post" action="newarticle_add.php">';
	echo '	<input id = "menu_btn" type="submit" name="submitButton" value="Добавить статью"/> </form>';
	echo '	<form class = "lft" method="post" action="users.php">';
	echo '	<input id = "menu_btn" type="submit" name="submitButton" value="Пользователи"/> </form>';
	echo '	<form class = "lft" method="post" action="stat.php">';
	echo '	<input id = "menu_btn" type="submit" name="submitButton" value="Статистика"/> </form>';
}


echo '</div>';
//echo '	<form class = "lft" method="post" action="ident.php">';
echo '<br>';
echo '<br>';





?>