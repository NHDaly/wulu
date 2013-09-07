<?php
  echo "url : " . $_POST["url"];
$content = file_get_contents('http://tts-api.com/tts.mp3?q=hello+nathan');
$file = "sound.mp3";
file_put_contents($file, $content);
?>
