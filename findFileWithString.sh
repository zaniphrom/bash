#!/bin/bash

#***Find Ghost mark up in files*****

FOLDER="/root/ghost"
STRING="post-excerpt"

cd $FOLDER
PWD=`pwd`
echo "working directory = $PWD"

ANOTHER=`egrep -lir --include=*.{hbs,php,html,js} "($STRING)" .`
echo $ANOTHER

# exit 0