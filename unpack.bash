./unspendable.py TiNYURLdCoMsJRiGLERz D 30 | while read LINE
do
   echo $LINE
   LINE=$(echo $LINE | sed 's/c/\:/g');
   LINE=$(echo $LINE | sed 's/s/\//g');
   LINE=$(echo $LINE | sed 's/d/\./g');
   LINE=$(echo $LINE | sed 's/h/\http/g');
   LINE=$(echo $LINE | sed 's/c/\:/g');
   LINE=$(echo $LINE | sed 's/c/\:/g');
   LINE=$(echo $LINE | sed 's/z.*//g');
   echo $LINE | cut -c 2- | tr 'A-Z' 'a-z'
done 
