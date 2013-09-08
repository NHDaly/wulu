<?php
# argv[1] = title
# argv[2] = site url
// Replace with proper user, password, and host.
$user = 'root'; 
$password = 'pennapps2013';
# $password = 'root';
$host = 'localhost';
# $host = ':/Applications/MAMP/tmp/mysql/mysql.sock';
$link = mysql_connect($host, $user, $password) or die(mysql_error());;
@mysql_select_db("wuludb", $link) or die('Could not connect: ' . mysql_error());
// Check connection.
if (mysqli_connect_errno($link)){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
// Sanitize input, and then insert title and site_url to the database.
$podcast = mysql_real_escape_string($argv[1]);
$title =  mysql_real_escape_string($argv[2]);
$site_url =  mysql_real_escape_string($argv[3]);
$pubdate = mysql_real_escape_string($argv[4]);
$query = "INSERT INTO Episodes VALUES ('" . $podcast . "', '" . $title . "', '" . $site_url . "', '', '" . $pubdate . "')";

$result = mysql_query($query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}
mysql_close($link);
?>
