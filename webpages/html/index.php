<html>
	<head>
		<title>WuLu Podify</title>
		<link rel="stylesheet" type="text/css" href="../css/index.css"/>
		<script src="../js/jquery-1.10.1.min.js"></script>
		<script src="../js/index.js"></script>
	</head>
	<body>
	
		
		<span id="warning"> Sorry, the URL you have given does not have a RSS feed for you to subscribe to. </span> 

		<div id="url_form_wrapper"> 
		</div>
			<form  id="url_form" action="process_url.php" method="post">
				<input id="url_input" type="text" name="url" value="Input URL">
				<span id="url_submit_button">Submit</span>
				<input id="url_submit" type="submit">
				<img src="../images/loader.gif" id="loader">
			</form>
			<span id="result"> </span>

			<img src="../images/catbadge.jpeg" id="cat">
	</body>

</html>

