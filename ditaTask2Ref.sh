#!/usr/bin/sh

*convert task topics to reference topics***

#***define variables****
EDIT_DIR="/cygdrive/c/tasktest"

TASK="Task"
TASKLOWER="task"
TASKBODY="referencebody" #this is because task to reference ends up replacing it in the tag

STEPS="<steps>"
STEPS1="<\/steps>"
OLSTEPS="<p><ol>"
CLOSTEPS="<\/ol><\/p>"
STEP="step"
CMD="cmd"

EMPTY="< >"
EMPTY1="<\/ >"

REFSYN="refsyn"
CONTEXT="context"
RM=" "
REFERENCE="Reference"

INFO="<info>"
INFO1="<\/info>"
NOTE="<note>"
NOTE1="<\/note>"
POSTREQ="<postreq>"
POSTREQ1="<\/postreq>"

CTOFOL="<p><ol>" 
CTOFOL1="<\/ol><\/p>"
FCONT="<refsyn><p><ol>"
FCONT1="<\/ol><\/p><\/refsyn>" 

#***********

cd $EDIT_DIR
PWD=`pwd`
echo "working directory = $PWD"


FILES=`ls`
echo "The following files will be changed"
for i in $FILES
do 
echo "$i"
done

TMP="/tmp/$0.1"
trap "rm -f $TMP; echo 'removing $TMP'" 0 1 2 3 4 5 

#change time

for i in $FILES

do 
cat $i | sed -e "s/$TASK/$REFERENCE/g" -e "s/$TASKLOWER/reference/g" -e "s/$TASKBODY/refbody/g" -e "s/$CMD/$RM/g" -e "s/$STEPS/$OLSTEPS/g" -e "s/$STEPS1/$CLOSTEPS/g" -e "s/$STEP/li/g" -e "s/$CONTEXT/$REFSYN/g" -e"s/$EMPTY/$RM/g" -e "s/$EMPTY1/$RM/g" -e "s/$INFO/$NOTE/g" -e "s/$INFO1/$NOTE1/g" -e "s/$POSTREQ/$NOTE/g" -e "s/$POSTREQ1/$NOTE1/g" -e "s/$CTOFOL/$FCONT/g" -e "s/$CTOFOL1/$FCONT1/g" > $TMP 

mv -f $TMP $i
echo "first pass done check for errors\nTables will be screwed up"

done



