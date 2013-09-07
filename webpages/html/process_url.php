<?php
# echo "url : " . $_POST["url"];
# $content = file_get_contents('http://tts-api.com/tts.mp3?q=hello+nathan');
# $file = "sound.mp3";
# file_put_contents($file, $content);
error_reporting(E_ALL);
ini_set('display_errors', 'On');
# Run python script.
$url = $_POST["url"];
$url_json = exec('python ../../scripts/python/getFeedsFromUrl.py ' . $url); 
echo $url_json."<br>";

$url_obj=json_decode($url_json);
$count=count($url_obj);
echo "length: ".$count."<br>";

#assume count is one
if($count==0)
{ 
	header('Location: ./index.php?warning=1');
}
else #if($count==1)
{
	$string='python ../../scripts/python/createPodcastXml.py '.$url_obj[0];
	echo $string. "<br>";
	$xml_json=exec($string);
	#var_dump($xml_json);
	$xml_obj=json_decode($xml_json);
	echo $xml_obj['XML'];


    # once you have the args to add to database, run this command
    $args = "" # ... presumably you'll get this from json or something
    $spawnString = 'bash -c "exec nohup php addEpToDb.php '.$args.' < /dev/null > /dev/null 2>&1 &"';
    exec($spawnString);
}



?>
