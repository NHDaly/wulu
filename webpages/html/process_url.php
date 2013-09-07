<?php

phpinfo();

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

	$db_user="root";
	$db_password="pennapps2013";
	$database="wuludb"; 
	$db_cxn = pdo_connect('localhost', $db_user, $db_password); 
	@mysql_select_db($database, $db_cxn) or die('Could not connect: ' . mysql_error());  

	$query_podcast="SELECT * FROM Podcasts WHERE rss_url='".$folder_name."'";	

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
	
	echo 'python ../../scripts/python/createPodcastXml.py '.$url_json_obj[0]."<br>";
	
	$xml_json_obj=json_decode($xml_json_str, true);

	if(!$row)
	{
		echo "creating new podcast.xml <br>";
		file_put_contents($directory."/podcast.xml", $xml_json_obj['XML']);
	}

	for($i=0; $i<count($xml_json_obj['episodes']); $i++)
	{ 
    # once you have the args to add to database, run this command
		# ... presumably you'll get this from json or something
#    $spawnstring = "bash -c 'exec nohup php addeptodb.php ".$folder_name." \"".$xml_json_obj['episodes'][$i]['title']."\" ".$xml_json_obj['episodes'][$i]['site_url']." \"".$xml_json_obj['episodes'][$i]['pub_date']."\" < /dev/null > /dev/null 2>&1 &'";

		$query_episode= "SELECT * FROM Episodes WHERE rss_url='".$folder_name."' AND title='".$xml_json_obj['episodes'][$i]['title']."' AND pub_date='".$xml_json_obj['episodes'][$i]['pub_date']."'";

		echo $query_episode."<br>";

		$result=mysql_query($query_episode, $db_cxn);

		$row=mysql_fetch_array($result);


		if(!$row)
		{
			$spawnstring = 'php addEpToDb.php '.$folder_name.' "'.$xml_json_obj['episodes'][$i]['title'].'" '.$xml_json_obj['episodes'][$i]['site_url'].' "'.$xml_json_obj['episodes'][$i]['pub_date'].'" ';

			echo $spawnstring."<br>";
			exec($spawnstring); 

			

			$article_json_str = exec('python ../../scripts/python/urlToArticleText.py ' . $xml_json_obj['episodes'][$i]['site_url']); 
			$article_json_obj = json_decode($article_json_str, true);
			#make sure to check for null

			echo urlencode($article_json_obj);


			$tts_url='http://tts-api.com/tts.mp3?q='.urlencode($article_json_obj);
			$content = file_get_contents($tts_url);
			$file = $directory."/sound".$i.".mp3";
			file_put_contents($file, $content);


		}
	}


}



?>
