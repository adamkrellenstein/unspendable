if [[ $CIRCLE_CI == 'true' ]]
then
DIR=/home/circleci/project
else
DIR=/root/unspendable
fi
../unspendable.py D DDDDzzzzzzzzzzzzzzzzzzzzzzzz 30 | grep E4X3tx
