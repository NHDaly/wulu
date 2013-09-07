<?php
# argv[1] = title
# argv[2] = site url
// Replace with proper user, password, and host.
$user = 'root'; 
$password = 'root';
$host = ':/Applications/MAMP/tmp/mysql/mysql.sock';
$link = mysql_connect($host, $user, $password) or die(mysql_error());;
@mysql_select_db("wuludb", $link) or die('Could not connect: ' . mysql_error());
// Check connection.
if (mysqli_connect_errno($link)){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$query  = "INSERT INTO Episodes (title, site_url) Values ('" . $argv[1] . "', '" . $argv[2] . "')";
$result = mysql_query($query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}
mysql_close($link);
?>
