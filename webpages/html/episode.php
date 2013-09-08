<?php

	$directory=$argv[1];
	$rss_url=$argv[2];
	$title=$argv[3];
	$site_url=$argv[4];
	$pub_date=$argv[5];

	$db_user="root";
	$db_password="pennapps2013";
	$database="wuludb"; 
	$db_cxn = mysql_connect('localhost', $db_user, $db_password); 
	@mysql_select_db($database, $db_cxn) or die('Could not connect: ' . mysql_error());  



$query_episode= "SELECT * FROM Episodes WHERE rss_url='".$rss_url."' AND title='".$title."' AND pub_date='".$pub_date."'";

$result=mysql_query($query_episode, $db_cxn) or die($query_episode."<br/><br/>".mysql_error());

$row=mysql_fetch_array($result);


if(!$row)
{

	$spawnstring = 'php addEpToDb.php '.$rss_url.' "'.$title.'" '.$site_url.' "'.$pub_date.'" ';

	exec($spawnstring); 

	

	$article_json_str = exec('python ../../scripts/python/urlToArticleText.py ' . $site_url); 
	$article_json_obj = json_decode($article_json_str);
	#make sure to check for null
     
    #TODO get Unsquashed title
    #$episode_text = urlencode($title).'+,,,+'.urlencode($article_json_obj);
    $episode_text = urlencode($article_json_obj);

	$tts_url='http://tts-api.com/tts.mp3?q='.$episode_text;
	$content = file_get_contents($tts_url);
	$audio_name=$rss_url."-".preg_replace("/[^A-Za-z0-9]/", '', $title).".mp3";
	$file = $directory."/".$audio_name;
	file_put_contents($file, $content);
	
	$insert_audio_file_path="UPDATE Episodes SET audio_url='".$file."' WHERE rss_url='".$rss_url."' AND title='".$title."' AND pub_date='".$pub_date."'";

	mysql_query($insert_audio_file_path, $db_cxn) or die($query_episode."<br/><br/>".mysql_error()); 

	exec("python ../../scripts/python/updatePodcastWithDatabase.py ".$rss_url." '".$title."' ".$audio_name." '".$pub_date."'");
}


?>
