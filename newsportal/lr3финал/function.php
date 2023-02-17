<?php
function input_users()
	{
		$f = fopen('users.csv', 'r');
		$user_set = array();
		while (!feof($f))
		{
			$data = fgetcsv($f,1000,';');
			if ($data[0] !== NULL)
			{
				$user_set[] = $data;
			}
		}
		fclose($f);
		$_SESSION['users'] = $user_set;
		//print_r($users);
	}

	function input_categorys()
	{
		$f = fopen('categories.csv', 'r');
		$category_set = array();
		while (!feof($f))
		{
			$data = fgetcsv($f,1000,';');
			if ($data[0] !== NULL)
			{
				$category_set[] = $data;
			}
		}
		fclose($f);
		$_SESSION['categorys'] = $category_set;

	}

function output_categorys($categorys)
	{
		$f = fopen('category.csv', 'a');
		foreach($categorys as $value)
		{
			fputcsv($f, $value, ';');
		}
		fclose($f);
	}	
function output_articles($article_set)
	{
		$f = fopen('articl.csv', 'a');
		//foreach($articles as $value)
		//{
			fputcsv($f, $article_set, ';');
		//}
	}

	function output_users($user_set)
	{
		$f = fopen('users.csv', 'a');
		foreach($user_set as $value)
		{
			fputcsv($f, $value,';');
		}
		fclose($f);
	}
		function input_statist()
	{
		$file = fopen('articl.csv', 'r');
		$statist = array();
		while (!feof($file))
		{
			$a = fgetcsv($file,1000,';');
			if ($a[0] !== NULL)
			{
				$statist[] = $a[6];
			}
		}
		fclose($file);
		$_SESSION['statist'] = $statist;
	}
		function input_articles()
	{
		$file = fopen('articl.csv', 'r');
		$articles = array();
		while (!feof($file))
		{
			$a = fgetcsv($file,10000,';');
			if ($a[0] !== NULL)
			{
				$articles[] = $a;
			}
		}
		fclose($file);
		$_SESSION['articles'] = $articles;
	}

	function input_comment()
	{
		$f = fopen('comments.csv', 'r');
		$set = array();
		while (!feof($f))
		{
			$data = fgetcsv($f,1000,';');
			if ($data[0] !== NULL)
			{
				$set[] = $data;
			}
		}
		fclose($f);
		$_SESSION['comments'] = $set;
		//print_r($users);
	}
	function output_comment($article_set)
	{
		$f = fopen('comments.csv', 'a');
		//foreach($articles as $value)
		//{
			fputcsv($f, $article_set, ';');
		//}
	}