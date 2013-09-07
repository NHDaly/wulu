<?php
# argv[1] = title
# argv[2] = site url
// Replace with proper user, password, and host.
$user = 'wulu'; 
$password = 'wulu';
$link = mysql_connect('localhost', $user, $password) or die(mysql_error());;
@mysql_select_db("wuludb", $link) or die('Could not connect: ' . mysql_error());
// Check connection.
if (mysqli_connect_errno($link)){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
// Insert title and site_url to the database
$query  = "INSERT INTO Episodes VALUES ('" . $argv[1] . "', '" . $argv[2] . "', '" . $argv[3] . "', '', '" . $argv[4] . "')";

$result = mysql_query($query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}
mysql_close($link);
?>
