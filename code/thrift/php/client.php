<?php
error_reporting(E_ALL);

$GLOBALS['THRIFT_ROOT'] = dirname(__FILE__).'/lib';
require_once $GLOBALS['THRIFT_ROOT'].'/Thrift.php';
require_once $GLOBALS['THRIFT_ROOT'].'/protocol/TBinaryProtocol.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TSocket.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/THttpClient.php';
require_once $GLOBALS['THRIFT_ROOT'].'/transport/TBufferedTransport.php';

$GEN_DIR = dirname(__FILE__).'/../gen-php';
require_once $GEN_DIR.'/service_types.php';
@require_once $GEN_DIR.'/UserStorage.php';

try {
  $socket = new TSocket('localhost', 9090);
  $transport = new TBufferedTransport($socket, 1024, 1024);
  $protocol = new TBinaryProtocol($transport);
  $client = new UserStorageClient($protocol);

  $transport->open();

  $user = $client->retrieve(1);
  var_dump($user);

  $new_user = new example_UserProfile(array(
    "uid" => '123',
    "name" => "Ralph Waldo Emerson",
    "style" => example_MartialArt::KARATE
  ));
  $client->store($new_user);
  $transport->close();

} catch (TException $tx) {
  print 'TException: '.$tx->getMessage()."\n";
}

?>
