<?php 
include 'function.php';

session_start();
include "header.php";
echo '<link rel="stylesheet" href="article.css" media="screen" type="text/css">';

input_articles();
$articles = $_SESSION['articles'];
echo '<div >';
foreach ($articles as $value) {
		echo ' <div class="article">';
		echo ' <div class="title">';
			echo '<h3>',$value[1],'</h3>';
		echo '</div>';
		echo ' <div class="author">';
			echo '<p>',$value[0],'</p>';
		echo '</div>';
		echo ' <div class="text">';
			echo '<a href ="article.php?id=',$value[5],'">Читать полностью</a>';
		echo '</div>';
		echo '</div>';
}

echo '</div>';';

 ?>';