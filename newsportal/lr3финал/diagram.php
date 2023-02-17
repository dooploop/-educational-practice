<?php
include "function.php";


	session_start();

	if (!isset($_SESSION['articles']))
	{
		input_articles();
	}
	if (!isset($_SESSION['statist']))
	{
		input_statist();
	}
	
	$statist = $_SESSION['statist'];
	$articles = $_SESSION['articles'];
	
	$sum = 0;
	for ($i = 0; $i < count($statist); $i++)
	{
		$sum = $sum + $statist[$i][0];
	}

	$w = 1200;
	$h= $sum*25;
	$roww = 50;
	$rowInterval = 10;

	$image = imagecreatetruecolor($w, $h);
	$white = imagecolorallocate($image, 220, 225, 225); 
	imagefill($image, 0, 0, $white);

	for($i = 0, $y1 = $h, $x1 = 0; $i < count($statist); $i++) {
	  $color = imagecolorallocate($image, rand(0, 255), rand(0, 255), rand(0, 255)); 

	  $y2 = $y1 - $statist[$i][0]*$h/$sum;
	  $x2 = $x1 + $roww;
	  imagefilledrectangle($image, $x1, $y1, $x2, $y2, $color);
	  $x1 = $x2 + $rowInterval;
	}

	header ("Content-type: image/gif"); 
	imagegif($image);
?>