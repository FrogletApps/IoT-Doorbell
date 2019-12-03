<!DOCTYPE html>
<html lang="en-gb">

	<head>
		<title>Pi Spy Images</title>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">

		<link rel="icon" href="https://frogletapps.github.io/Assets/favicon.ico" type="image/ico">
		<link rel="stylesheet" type="text/css" href="https://frogletapps.github.io/Assets/FrogletApps.css">
		<link rel="stylesheet" type="text/css" href="iotDoorbell.css">
	</head>
	<body>
		<div id="topBar">
			<h1>Pi Spy Images</h1>
		</div>

		<br><br>

		<!--<div class="buttonHolder">
			<form method="post">
				<input type="submit" name="test" value="Take a picture"/>
			</form>
		</div>

		<?php
			#if(array_key_exists('test',$_POST)){
			#	shell_exec('../pi/picture.py');
			#	unset($_POST['test']);
			#}
		?>

		<br><br>-->

		<?php
			$dirname = "DoorbellPics/";
			$images = array_reverse(glob($dirname . "*.jpg"));
			foreach($images as $image) {
				echo '<p>'.explode("/", $image)[1].'</p>';
				echo '<img class="doorbellPics" src="'.$image.'" />';
				echo '<br><br>';
			}
		?>
		
		<div class="topcorner">
			<a href="/">
				<img alt="Back" class="back" src="/back.png">
			</a>
		</div>
	</body>
</html>
