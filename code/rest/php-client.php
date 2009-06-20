<?php
include("php-rest-service/user.php");

function get($url) {
  $session = curl_init($url);
  curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
  $response = curl_exec($session);
  curl_close($session);
  
  return $response;
}

function post($url, $postargs) {
  $session = curl_init($url);
  curl_setopt ($session, CURLOPT_POST, true);
  curl_setopt ($session, CURLOPT_POSTFIELDS, $postargs);
  curl_setopt($session, CURLOPT_RETURNTRANSFER, true);
  $response = curl_exec($session);
  curl_close($session);

  assert($response == "OK");
  return $response;
}

function decode_user($user_data) {
  $args = json_decode($user_data);
  $user = new User($args->id, $args->name, $args->style);
  assert($user->id == 27);
  return $user;  
}

function encode_user() {
  $id = 27;
  $name = "luis inacio";
  $style = MartialArt::$KARATE;
  $postargs = 'id=' . urlencode($id) . '&name=' . urlencode($name).'&style='.urlencode($style);  
  return $postargs;
}


function rest_benchmark() {
  $server = "http://localhost/service/";
  $get_url = $server . "user_get.php?user_id=27";
  $post_url = $server . "user_post.php";

  for ($i=0; $i<1000; $i++) {
    for ($j=0; $j<9; $j++) {
      decode_user(get($get_url));
    }
    post($post_url, encode_user());
    if ($i % 100 == 0) {
      echo $i;
      echo "\n";
    }
  }
}

function benchmark($server) {
  for ($i=0; $i<10000; $i++) {
    $response = get($server);
    if ($i % 1000 == 0) {
      echo $i;
      echo "\n";
    }
  }  
}

function dynamic_benchmark() {
  $server = "http://localhost/service/dynamic.php";
  benchmark($server);
}

function json_benchmark() {
  $server = "http://localhost/service/user_get.php?user_id=27";
  benchmark($server);
}

function static_benchmark() {
  $server = "http://localhost/service/static.html";
  benchmark($server);
}

switch ($argv[1]) {
  case "dynamic":
    dynamic_benchmark();
    break;
  case "json":
    json_benchmark();
    break;
  case "rest":
    rest_benchmark();
    break;
  case "static":
    static_benchmark();
    break;
  default: 
    echo "ooops, nothing do to do here..";
}

?>
