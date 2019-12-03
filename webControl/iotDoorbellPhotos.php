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

	<?php
		$dirname = "DoorbellPics/";
		$images = glob($dirname . "*.jpg");
		foreach($images as $image) {
			//echo '<p>'.$image.'</p>'
			echo '<img src="'.$image.'" />';
			echo '<br><br>'
		}
	?>
	
	<div class="topcorner"><a href="iotDoorbell.html">Home</a></div>
</html>
