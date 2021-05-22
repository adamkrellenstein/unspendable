if [[ $CIRCLECI == 'true' ]]
then
DIR=/home/circleci/project
else
DIR=/root/unspendable
fi

T="a,b,c. d:e-f"
CMD=$DIR/unspendable.py

for X in DAx DBx DCx DEx DFx DGx DHx DJx DKx DLx DMx DNx DPx DQx DRx DSx DTx 
  do
  $CMD $X "$T"
  done  

