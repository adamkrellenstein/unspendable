#!/bin/bash
echo "Content-type: text/html"
echo
echo "<pre>"
echo "<h1>DiMECASH Address</h1>"

echo "<div>The following valid Dogecoin, Digibyte, Verge, etc."
echo "address is NOT to be used as a store of value. Only use"
echo "this system with very small transactions to hold data. No"
echo "private key exists to retrieve any funds sent to this"
echo "address.</div><hr>"

name=$(echo $QUERY_STRING | sed 's/&/ /g' )
name=$(echo $name | sed 's/\%20/ /g')
name=$(echo $name | sed 's/\%22/"/g')
#name=$(echo $name | sed 's/+/ /g')
eval $name > /dev/null
final=$(echo $rest | sed 's/+/ /g')
VAL=$(python3 ./unspendable.py DCx "$final")

echo $VAL
/usr/local/bin/qr $VAL > /var/www/html/images/$VAL

echo "<img src=../images/$VAL width='80px' height='80px'>"

: Ethereum version
echo "<h2>Ethereum Testnet Transaction</h2>"
ETH1=$(echo $VAL | cut -c 1-27 | base58 -d | xxd -p)
ETH2=$(echo $VAL | cut -c 28- | base58 -d | xxd -p)
echo "0x$ETH1"
echo


: Return
echo "<a href=/unspendable.html>Go back and do another</a>"


#echo "<meta http-equiv='refresh' content='0;URL=https://dime.cash/unsp.php?name=$VAL'>"
# echo "<meta http-equiv='refresh' content='0;URL=https://dime.cash/?page_id=71&address=$VAL'>"
