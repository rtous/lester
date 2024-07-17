#EXAMPLE: ./lowpoly.sh green_woman3 1
#EXAMPLE: ./lowpoly.sh man_walk_1_part1 0
#EXAMPLE: ./lowpoly.sh green_woman1 5

SCENE_NAME=$1
ADDFACE=$2
SHADOWSIZE=$3
python lowpoly_last.py $SCENE_NAME $ADDFACE $SHADOWSIZE