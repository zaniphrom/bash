#!/bin/bash
#
# A script to update a new VM to my usual needs
# (Tested on Ubuntu 12.04)

# Ask for new user password
	echo -e "enter the filepath of the folder you wish to make changes in:\c"
	read PASSWD
 
# To download this script

# wget -c http://chromedriver.googlecode.com/files/chromedriver_linux64_2.1.zip 
 
# Usual update
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get -y install python python-pip
sudo pip install beautifulsoup4


# make new user with sudo rights and home directory

useradd -m -s /bin/bash -d /home/brian -U brian -p $PASSWD



