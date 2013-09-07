<?php


$url = './index.php?warning=2';
$u1='google.com';
$u2='yahoo.com';
$myvars = 'url1=' . $u1 . '&url2=' . $u2;

$ch = curl_init();
//curl_setopt( $ch, CURLOPT_POST, 1);
//curl_setopt( $ch, CURLOPT_POSTFIELDS, $myvars);
curl_setopt( $ch, CURLOPT_URL, $url);
curl_setopt( $ch, CURLOPT_HEADER, 0);
#curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);

$response = curl_exec( $ch );
echo "done";

?>
