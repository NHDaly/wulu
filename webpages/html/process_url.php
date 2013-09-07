<?php
# echo "url : " . $_POST["url"];
# $content = file_get_contents('http://tts-api.com/tts.mp3?q=hello+nathan');
# $file = "sound.mp3";
# file_put_contents($file, $content);
error_reporting(E_ALL);
ini_set('display_errors', 'On');
# Run python script.
$url = $_POST["url"];
$result = exec('python ../../scripts/python/getrssfeed.py ' . $url);
echo $result;
?>
