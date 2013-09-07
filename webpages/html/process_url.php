<?php
# echo "url : " . $_POST["url"];
# $content = file_get_contents('http://tts-api.com/tts.mp3?q=hello+nathan');
# $file = "sound.mp3";
# file_put_contents($file, $content);
error_reporting(E_ALL);
ini_set('display_errors', 'On');
# Run python script.
$url = $_POST["url"];
$url_json_str = exec('python ../../scripts/python/getFeedsFromUrl.py ' . $url); 

$url_json_obj=json_decode($url_json_str);
$count=count($url_json_obj);

#assume count is one
if($count==0)
{ 
	header('Location: ./index.php?warning=1');
}
else #if($count==1)
{

	$directory="../../../wulutestserver/podcasts/";
  $folder_name=preg_replace("/[^A-Za-z0-9 ]/", '', $url_json_obj[0]);

	$directory=$directory.$folder_name;	

	$db_user="wulu";
	$db_password="wulu";
	$database="wuludb"; 
	$db_cxn = mysql_connect('localhost', $db_user, $db_password); 
	@mysql_select_db($database, $db_cxn) or die('Could not connect: ' . mysql_error());  

	$query_podcast="SELECT * FROM Podcasts WHERE podcast='".$folder_name."'";	

	$result=mysql_query($query_podcast, $db_cxn);
	$row=mysql_fetch_array($result);

	if(!$row)
	{ 
		echo "creating new directory: ".$directory." <br>";
		exec('mkdir -p '.$directory); 
		$insert_podcast="INSERT INTO Podcasts VALUES ('".$folder_name."')";
		mysql_query($insert_podcast, $db_cxn);
	}



	$xml_json_str=exec('python ../../scripts/python/createPodcastXml.py '.$url_json_obj[0]);
	

	$xml_json_obj=json_decode($xml_json_str, true);

	if(!$row)
	{
		echo "creating new podcast.xml <br>";
		file_put_contents($directory."/podcast.xml", $xml_json_obj['XML']);
	}

	for($i=0; $i<count($xml_json_obj['episodes']); $i++)
	{
		echo $xml_json_obj['episodes'][$i]['title']."<br>";

	}


    # once you have the args to add to database, run this command
    #$args = "" 
		# ... presumably you'll get this from json or something
    #$spawnString = 'bash -c "exec nohup php addEpToDb.php '.$args.' < /dev/null > /dev/null 2>&1 &"';
    #exec($spawnString);
}



?>
