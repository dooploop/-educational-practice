<?php 
include "function.php";

$a = $_SESSION['delart'];
echo $a;
include "header.php";

		
input_categorys();
$categorys = $_SESSION['categorys'];

echo '<div class = "add_article_main">';

echo '<form class = "add_article" method="post">';

echo '<div class = "input">';

	echo '<input class="vvod" name = "name" type="text" placeholder="Название">';

echo '</div>';



echo '<div class = "choose_catt">';

	echo '<select class = "categor_add" name = "Категория">';
	for ($i = 0; $i < count($categorys); $i++)
	{
		echo '<option value = "'.$categorys[$i][0].'"> '.$categorys[$i][0].'</option>';
	}
	echo '</select>';

echo '</div>';




echo '<div class = "text_add">';
	
	echo '<textarea id="statya" name = "article" rows="20" cols="160" placeholder="Статья"></textarea><br>';

echo '</div>';




echo '<div class = "button_add">';

    echo '<input class="but" name = "add" type="submit" value="Добавить"></form>';
echo '</div>';


    if (isset($_POST['add'])) {
    	$flag1 = false;
		$flag2 = false;
		if (isset($_POST['name']))
		{
			$name = trim(filter_var($_POST['name'], FILTER_SANITIZE_STRING));
			$flag1 = true;
		}
		else
		{
			echo '<p>Не введено название статьи!</p>';
		}
		if (isset($_POST['article']))
		{
			$article = trim(filter_var($_POST['article'], FILTER_SANITIZE_STRING));
			$flag2 = true;
		}
		else
		{
			echo 'Не введен текст статьи!';
		}
		if ($flag1 && $flag2)
		{
			$categ = $_POST['Категория'];
			$today = date("d.m.Y");
			$author = $_SESSION['user'][0];//. ' '. $_SESSION['surname'];
			$new_article = array($author, $name, $today, $categ, $article,mt_rand(),0);
			//$articles[] = $new_article;
			//$statist[] = array(0);
			//unset($_SESSION['statist']);
			//output_statist($statist);
			//unset($_SESSION['articles']);
			output_articles($new_article);
			echo '<script language="javascript">';
			echo 'alert("Статья добавлена.")';
			echo '</script>';
    }
}
echo '</div>';
	
 ?>