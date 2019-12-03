<!DOCTYPE html>
<html lang="en-gb">

	<head>
		<title>Pi Spy Admin</title>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">

		<link rel="icon" href="https://frogletapps.github.io/Assets/favicon.ico" type="image/ico">
		<link rel="stylesheet" type="text/css" href="https://frogletapps.github.io/Assets/FrogletApps.css">
		<link rel="stylesheet" type="text/css" href="/iotDoorbell.css">
	</head>
	
	<body>
		<div id="topBar">
			<h1>Pi Spy Admin</h1>
		</div>
		
		<br><br>
		
		<div class="buttonHolder">
			<button onclick ="window.location = 'Tasks/reboot.php';"<p>Reboot</p></button>
			<button onclick ="window.location = 'Tasks/shutdown.php';"<p>Shutdown</p></button>
		</div>

		<!--This is external code to print the client's IP address-->
		<script type="text/javascript" src="https://l2.io/ip.js?var=userip"></script>
			
			<p><script type="text/javascript">
			var userip;
			document.write("Your IP is: ", userip);
		</script></p>
		
		<!-- This is PHP to print the name of the server -->
		<p>The server IP is:  
		<?php
			echo $_SERVER['SERVER_NAME'];
		?>
		</p>
		<br>

		<div class="topcorner">
			<a href="/">
				<img alt="Back" class="back" src="/back.png">
			</a>
		</div>
	</body>
</html>
