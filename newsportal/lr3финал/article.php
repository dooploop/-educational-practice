<?php  
include "header.php";
include "function.php";


//unset($_POST['add_comment']);

//echo $_GET['id'];
$articles = $_SESSION['articles'];
echo '<div class = "obshiy">';

foreach ($articles as $value) {
	if ($value[5] == $_GET['id']) {
		$value[6] += 1;
		$_SESSION['viewadd'] = $value[6];

		echo ' <div class="article_f">';
		echo ' <div class="title_f">';

		echo '<h4>',$value[1],'</h4>';

		echo '</div>';

		
		echo ' <div class="text_f">';
		echo '<p>',$value[4],'</p>';

		echo '</div>';
		echo ' <div class="author_f">';
			echo '<p class = "author_name"> Автор: ',$value[0],'</p>';
			echo '<p class = "author_name"> Категория: ',$value[3],'</p>';

			echo '<p class = "author_name"> Просмотры: ',$value[6],'</p>';

		echo '</div>';
		echo '</div>';


		/*echo '	<form action = "#" method="POST">';
		echo '	<input id = "menu_btn" type="submit" name="',$value[5],'" value="Удалить"/> ';
		
	echo '	</form>';*/

}

}
if (isset($_SESSION['viewadd'])) {
	$file = fopen('articl.csv', 'w');

	for ($i=0; $i <count($articles); $i++) { 
		if ($articles[$i][5] == $_GET['id']){
			$articles[$i][6] = $_SESSION['viewadd'];

		}
			output_articles($articles[$i]);
	}
}
input_comment();
$comments = $_SESSION['comments'];

	echo '<div class="comments_of_article">';
	echo '<h1>Комментарии</h1>';
	foreach ($comments as $value) {
		if ($value[0] == $_GET['id']) {
	echo '<div class = "comment_block">';
		echo '<p>Автор: ',$value[1] ,'</p>';
		echo '<p>Текст комментария: ',$value[2] ,'</p>';
	echo '</div>';

	}
}

	echo '</div>';
	
	echo '<div class="comments">';
	echo '<form action="#" method="post">';
	echo '		<div>';
	//echo '			<label for="name">Text Input:</label>';
	//echo '			<input type="text" name="name" id="name" value="" tabindex="1" />';
	//echo '		</div>';
		
	echo '		<div>';
	echo '			<label for="textarea">Комментарий:</label>';
	echo '		</div>';
	echo '		<div>';
	
	echo '			<textarea cols="50"  rows="10" name="text_comment" id="textarea"></textarea>';
	echo '		</div>';
		
		
	echo '		<div>';
	echo '			<input type="submit" name = "add_comment" value="Добавить" id = "menu_btn2"/>';
	echo '		</div>';
	echo '	</form>';
	echo '</div>';
	if (isset($_POST['add_comment'])) {
		$com_text = $_POST['text_comment'];
		$username = $_SESSION['user'][0];
		$id_auth = $_GET['id'];
		$comment = array($id_auth,$username,$com_text);
		output_comment($comment);
		//unset($_POST['add_comment']);
 		echo "<meta http-equiv = 'refresh' content = '0'>";

	}

	
echo '</div>';

?>