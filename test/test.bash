unspendable_test() {

if [[ $CIRCLECI == 'true' ]]
then
DIR=/home/circleci/project
else
DIR=/root/unspendable
fi

CMD=$DIR/unspendable.py
T=DDxxDDDDDDDDD
for X in 1 2 3 4 5 6 7 8 9s 9t 9u 9v 9w 9x 9y 9z A B C D DC DCx E F G H J K mv
do
$CMD $X $T 
done  } 
unspendable_test | sum | grep 02023 
