<?php
# echo "url : " . $_POST["url"];
# $content = file_get_contents('http://tts-api.com/tts.mp3?q=hello+nathan');
# $file = "sound.mp3";
# file_put_contents($file, $content);
error_reporting(E_ALL);
ini_set('display_errors', 'On');
# Run python script.
$url = $_POST["url"];
$json = exec('python ../../scripts/python/getFeedsFromUrl.py ' . $url); 
echo $json."<br>";

$obj=json_decode($json);
$count=count($obj);
echo "length: ".$count."<br>";

#assume count is one

$string='python ../../scripts/python/createPodcastXml.py '.$obj[0];
echo $string. "<br>";
$xml=exec($string);
var_dump($xml);




?>
