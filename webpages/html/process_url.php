<?php

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
	echo "no_rss";
}
else #if($count==1)
{
	$directory=exec('python ../../scripts/python/constants.py site_abs_directory');
  $folder_name=preg_replace("/[^A-Za-z0-9 ]/", '', $url_json_obj[0]);

	$directory=$directory.$folder_name;	

	$db_user="root";
	$db_password="pennapps2013";
	$database="wuludb"; 
	$db_cxn = mysql_connect('localhost', $db_user, $db_password); 
	@mysql_select_db($database, $db_cxn) or die('Could not connect: ' . mysql_error());  
  
  $folder_name = mysql_real_escape_string($folder_name);
	$query_podcast="SELECT * FROM Podcasts WHERE rss_url='".$folder_name."'";	

	$result=mysql_query($query_podcast, $db_cxn) or die($query_podcast."<br/><br/>".mysql_error());
	$row=mysql_fetch_array($result);

	if(!$row)
	{ 
		mkdir($directory) or die ("mkdir(".$directory."): "."error"); 
		$insert_podcast="INSERT INTO Podcasts VALUES ('".$folder_name."')";
		mysql_query($insert_podcast, $db_cxn) or die($insert_podcast."<br/><br/>".mysql_error());

	}



	$xml_json_str=exec('python ../../scripts/python/createPodcastXml.py '.$url_json_obj[0]);
	
	
	$xml_json_obj=json_decode($xml_json_str, true);

	if(!$row)
	{
		file_put_contents($directory."/podcast.xml", $xml_json_obj['XML']);
	}


    ######OLD NON FORKING CODE FROM HACKATHON###### 

	for($i=0; $i<min(5,count($xml_json_obj['episodes'])); $i++)
	{ 
		$rss_url=$folder_name;
        $episode_json = $xml_json_obj['episodes'][$i];
        $episode_json_str = json_encode($episode_json);
        $epCommand = "php ./episode.php '".$directory."' '".$rss_url."' '".$episode_json_str."' &> /dev/null &"; 
        exec($epCommand); 
	}


   #######NON-WORING FORKING CODE (apparently pcntl is not installed?) ####### 
	#for($i=0; $i<min(5,count($xml_json_obj['episodes'])); $i++)
	#{ 
    #    $pid = pcntl_fork();
    #    if ($pid == -1) 
    #    {
    #        die('could not fork');
    #    } 
    #    else if ($pid) 
    #    {
    #        // we are the parent
    #    } 
    #    else 
    #    {
    #        // we are the child
    #        $rss_url=$folder_name;
    #        $title=$xml_json_obj['episodes'][$i]['title'];
    #        $pub_date=$xml_json_obj['episodes'][$i]['pub_date'];
    #        $site_url=$xml_json_obj['episodes'][$i]['site_url']; 
    #        $epCommand = "php ./episode.php '".$directory."' '".$rss_url."' '".$title."' '".$site_url."' '".$pub_date."' &> /dev/null &"; 
    #        exec($epCommand); 
    #        exit();
    #    }



	#}




	$podcasts_addr=exec('python ../../scripts/python/constants.py podcasts_folder_address');
echo $podcasts_addr.$folder_name."/podcast.xml";
#	header('Location: ./end.php');

}



?>

