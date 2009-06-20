<?php
include("user.php");

$id = $_POST["id"];
$name = $_POST["name"];
$style = $_POST["style"];

$user = new User($id, $name, $style);
if ($user->id == 27) {
  echo "OK";
} else {
  echo "Validation Failed";
}

?>
