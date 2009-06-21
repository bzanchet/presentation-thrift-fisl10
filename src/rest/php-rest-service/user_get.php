<?php
include("user.php");

//find user
if ($_GET["user_id"] == 27) {
  $user = new User($_GET["user_id"], "luis inacio", MartialArt::$KARATE);
  echo json_encode($user);
}

?>
