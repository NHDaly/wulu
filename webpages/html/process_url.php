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
if($count==0)
{ 
	header('Location: ./index.php?warning=1');
}
else #if($count==1)
{
	$string='python ../../scripts/python/createPodcastXml.py '.$obj[0];
	echo $string. "<br>";
	$json=exec($string);
	var_dump($json);

    # once you have the args to add to database, run this command
    $args = "" # ... presumably you'll get this from json or something
    $spawnString = 'bash -c "exec nohup php addEpToDb.php '.$args.' < /dev/null > /dev/null 2>&1 &"';
    exec($spawnString);
}



?>
