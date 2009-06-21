<?php

class MartialArt {
  public static $AIKIDO = 1;
  public static $KARATE = 2;  
}

class User {
  var $id;
  var $name;
  var $style;

  function __construct($id, $name, $style) {
    $this->id = $id;
    $this->name = $name;
    $this->style = $style;
  }
}

