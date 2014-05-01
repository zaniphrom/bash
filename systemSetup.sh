#!/bin/bash
# A script to update a new VM to my usual needs
# Python Selenium BeautifulSoup
# To download this script
# sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/systemSetup.sh && chmod 775 systemSetup.sh
#echo -e "enter user password: "
#read PASSWD

#Usual home dir
BRIANHOME="/home/brian"

#Run as root
if [ `whoami` != "root" ] ; then
    echo "You must run this script as root. Goodbye."
    echo ""
    exit 1
fi

# Set up home dir

	if [ -e "$BRIANHOME" ] ; then 
		echo "Home directory already exists"
	else 
		sudo useradd -m -s /bin/bash -d /home/brian -U brian 
		sudo usermod -a -G sudo brian
		echo "Usual homedir made /home/brian"
	fi


# Usual update
	sudo apt-get -y update
	sudo apt-get -y dist-upgrade

# Usual installs
	sudo apt-get -y install python python-pip
	sudo apt-get -y install unzip
	sudo pip install beautifulsoup4
	sudo pip install selenium
	sudo pip install html5lib

	sudo apt-get -y install firefox
	sudo apt-get -y install google-chrome
	sudo apt-get -y install openjdk-7-jre
	sudo apt-get -y install xvfb imagemagick x11vnc 

#Reminder to change user password
	clear
	echo "Change the brian user password"

#If java command is available in the PATH (environment variable), you can start the Selenium server using this command:
# java -jar selenium-server-standalone-2.x.x.jar


# How to start on display 10
# sudo Xvfb :10 -ac
# export DISPLAY=:10
# firefox

