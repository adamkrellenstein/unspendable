<?php

$chord = file($argv[1]);

$lines = count($chord);
$thisline = 1;
$amount = "0.0001";

echo "/usr/local/bin/dogecoin-cli sendmany \"\" \"{\\\n";
foreach($chord as $line)
   {
     $address = chop($line);
//   list($address,$amount) = explode(" ",$line);
//   $amount = chop($amount);

   if($thisline == $lines)
        $ending = '}"';
             else
        $ending = ',\\';

   echo "\\\"$address\\\":$amount$ending\n";
   $thisline = $thisline + 1;
   }

?>
