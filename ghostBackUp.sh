#!/bin/bash
# A bach script to back up the ghost blogs content
# To download this script
# sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/ghostBackUp.sh && chmod 775 ghostBackUp.sh

#Define date
NOW=$(date +"%Y-%m-%d")
BACKUPDIR="/home/brian/$NOW"
BACKUPTAR="$BACKUPDIR.tar.gz"
	clear
	echo -e "Backing up data to the following directory\n$BACKUPDIR \n\nplease wait...\n"

#Define backup location

#Define the paths to the folders
BRIANPATH="/var/www/ghost"
BRIANCVPATH="/var/www/ghost_cv"
SONJAPATH="/var/www/ghost_sonja"

# Set up backup dir

	if [ -e "$BACKUPTAR" ] ; then 
		echo -e "This backup directory already exists: $BACKUPTAR"
		echo -e "You need to double check this before going ahead\n"
		exit 1
	else
		mkdir -p $BACKUPDIR
		cd $BACKUPDIR
		mkdir brian sonja cv 
	fi

#backup the config.js file and the contents/images and contents/themes directories
#for each ghost instance

# back up brian

	if [ -e "$BRIANPATH" ] ; then 
		cd $BRIANPATH
		cp index.js $BACKUPDIR/brian
		cp -r content/themes $BACKUPDIR/brian
		cp -r content/images $BACKUPDIR/brian
		echo -e "Backing up $BRIANPATH"
	else
		echo -e "$BRIANPATH DOESN'T EXIST!!You need to double check this before going ahead"
		exit 1
	fi

# back up sonja

	if [ -e "$SONJAPATH" ] ; then 
		cd $SONJAPATH
		cp index.js $BACKUPDIR/sonja
		cp -r content/themes $BACKUPDIR/sonja
		cp -r content/images $BACKUPDIR/sonja
		echo -e "Backing up $SONJAPATH"
	else
		echo -e "$SONJAPATH DOESN'T EXIST!!You need to double check this before going ahead"
		exit 1
	fi

# back up CV

	if [ -e "$BRIANCVPATH" ] ; then 
		cd $BRIANCVPATH
		cp index.js $BACKUPDIR/cv
		cp -r content/themes $BACKUPDIR/cv
		cp -r content/images $BACKUPDIR/cv
		echo -e "Backing up $BRIANCVPATH"
	else
		echo -e "$BRIANCVPATH DOESN'T EXIST!!You need to double check this before going ahead"
		exit 1
	fi

# Finally - compress the backup and remove the directory
	tar -zcf /home/brian/$NOW.tar.gz $BACKUPDIR
	rm -rf $BACKUPDIR 
	
ACHIEVED="You have backed up the contents of the above folders\n --> images, themes, and any changes to default files"
WARNING="WARNING: You need to back up the DB seperately\nUse the www.your.blog/ghost/debug page to export it"
	
	echo -e "\n$ACHIEVED"
	echo -e "\n$WARNING"