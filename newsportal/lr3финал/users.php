<?php 
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
	function output_users($user)
	{
		$file = fopen('users.csv', 'w');
		foreach($user as $value)
		{
			fputcsv($file, $value,';');
		}
		fclose($file);
	}

//$flag='false';

//unset($_SESSION['users']);
input_users();
$users = $_SESSION['users'] ;
	echo '<table class = "user_table">';
	echo '<tr>';

	echo '<td>ИМЯ	</td>';
    #echo '<td>Пароль	</td>';
    echo '<td>Никнейм	</td>';
    echo '<td>ID	</td>';
	echo '</tr>';

foreach($users as $value){
    

	echo '<tr>';
	echo '<td>',$value[0],'</td >'; 
	#echo '<td>',$value[1],'</td> ';
	echo '<td>',$value[2],'</td> ';
	echo '<td>',$value[3],'</td> ';
	//echo '<br>';
	
		# code...
	echo '	<form class = "del_but" method="GET">';
	if ($_SESSION['user'][4]==1) {
	echo '<td> <input id = "menu_btn" type="submit" name="',$value[3],'" value="Удалить"/></td> </form>';
}
	echo '	<form class = "adm_but" method="GET">';

	if ($_SESSION['user'][4]==1) {
			echo '<td> <input id = "menu_btn" type="submit" name="',$value[2],'" value="Сделать Администратором"/></td> </form>';
}
	echo '</tr>';
}
	echo '</table>';
	foreach ($users as $value)
			{
		if (isset($_GET[$value[3]])) {
			
			$_SESSION['del'] = $value[3];

		}
		if (isset($_GET[$value[2]])) {
			$_SESSION['adm'] = $value[2];
			
	}
}
		for ($i=0; $i <count($users); $i++) { 
		if ($users[$i][3]==$_SESSION['del']) {
			unset($users[$i]);
			output_users($users);
			echo "<meta http-equiv = 'refresh' content = '0'>";

		

		}
	}


		for ($i=0; $i <count($users); $i++) { 
		if ($users[$i][2]==$_SESSION['adm']) {
			$users[$i][4] = 1;
			//unset($users[$i]);

			output_users($users);
			//echo "<meta http-equiv = 'refresh' content = '0'>";
			break;

		}
	}
	
			//output_users($users);
		//	echo "<meta http-equiv = 'refresh' content = '0'>";


 ?>