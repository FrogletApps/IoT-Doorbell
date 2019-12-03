<html>
	<head>
		<title>IoT Doorbell Images</title>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">

		<link rel="stylesheet" type="text/css" href="https://frogletapps.github.io/Assets/FrogletApps.css">
		<link rel="stylesheet" type="text/css" href="iotDoorbell.css">
	</head>

	<div id="topBar">
		<h1>IoT Doorbell Photos</h1>
	</div>

	<br><br>

	<form method="post">
		<input type="submit" name="test" value="Take a picture"/>
	</form>

	<?php
		if(array_key_exists('test',$_POST)){
			shell_exec('../pi/picture.py')
			unset($_POST['test']);
		}
	?>

	<br><br>

	<?php
		$dirname = "DoorbellPics/";
		$images = array_reverse(glob($dirname . "*.jpg"));
		foreach($images as $image) {
			echo '<p>'.$image.'</p>';
			echo '<img src="'.$image.'" />';
			echo '<br><br>';
		}
	?>
	
	<div class="topcorner"><a href="iotDoorbell.html">Home</a></div>
</html>
