#!/usr/bin/sh

# This scripts will ask for variables and then change those specified in files within a folder
# When working in dita it essentially takes one set of files, creates new file names, and within th files
# resets the conrefs so that the single sourcing linking is already done

# set up fixes
NULL=""; export NULL #if user enters empty string

# get variables 
# Get file path
	echo -e "enter the filepath of the folder you wish to make changes in:\c"
	read FOLDER
#FOLDER="/cygdrive/c/Doc*/brianler/desktop/empirix"

# get first text variable
	echo -e "For first change enter the text to be replaced:\c"
	read OLDTEXT
	echo -e "For first change enter the replacement text:\c"
	read REPLACE

#get second text variable
echo -e "For second change enter the text to be replaced:\c"
read ADD1
	echo -e "For second change enter the replacement text:\c"
	read ADD2

#get file name part to be changed
	echo -e "enter filename to be changed:\c"
	read STEM
	echo -e "enter new filename part:\c"
	read STEMCHANGE

# check to see if folder specified is a valid folder
#if [ "$FOLDER" != 0 ] ; then 
#if [ "$FOLDER" != 0 ] ; then 
if [ -z "$FOLDER" ] ; then
	echo -e "WARNING!! \n $FOLDER is not a valid folder, please recheck and then :\n enter filepath here:\c"
	read FOLDER 
	echo -e "\n In this folder:\t $FOLDER"
else
	echo -e "\n In this folder:\t $FOLDER"
fi 

# set up traps
TMP="/tmp/$0.1"
TMP2="/tmp/$0.2"
TMP3="/tmp/$0.3"
trap "rm -f $TMP $TMP2 $TMP3 ; echo 'removing traps'" 0 1 2 3 4 5 

echo -e "\n You are changing:\t $OLDTEXT to $REPLACE"
echo -e "\n You are changing:\t $ADD1 to $ADD2"
echo -e "For file names you are changing:\n \t $STEM to $STEMCHANGE"

echo -e "\n do you wish to proceed [y|n]"
read ANS
[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
#need to fix that and also the mistake statements

## now to work in the files

cd $FOLDER
mkdir -p ../backup  
cp -Rn $FOLDER ../backup 

FILES=`find . -type f`
for i in $FILES
do 
	if [ -f $i ] ; then
	cat $i | sed -e "s/$OLDTEXT/$REPLACE/g" -e "s/$ADD1/$ADD2/g" > $TMP 
		if [ -s $TMP ] ; then
		#mv -n $i backup ; mv $TMP `echo $i | sed "s/$STEM/$STEMCHANGE/"`
		mv $i $TMP3 ; mv $TMP `echo $i | sed "s/$STEM/$STEMCHANGE/"`
	fi	
	fi
done
