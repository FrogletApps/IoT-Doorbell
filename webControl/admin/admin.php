<html>
	<head>
		<title>Admin Controls</title>
		<link rel="stylesheet" type="text/css" href="/iotDoorbell.css">
		<meta charset="UTF-8" name = "viewport" content="device-width, initial-scale=1.0">
	</head>
	
	<body>
		<h2>Admin Controls</h2>
		
		<div class="buttonHolder">
			<button onclick ="window.location = 'Tasks/reboot.php';"<p>Reboot</p></button>
			<button onclick ="window.location = 'Tasks/shutdown.php';"<p>Shutdown</p></button>
			<button onclick ="window.location = 'Tasks/update.php';"<p>Update</p></button>
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

		<div class="topcorner"><a href="/">Home</a></div>
	</body>
</html>
