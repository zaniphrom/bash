#!/bin/bash

# A script to update a new VM to my usual needs
# To download this script
# sudo wget -c https://github.com/zaniphrom/bash/blob/master/systemSetup.sh && chmod 775 systemSetup.sh
echo -e "enter user password: "
read PASSWD
useradd -m -s /bin/bash -d /home/brian -U brian -p $PASSWD
echo "User created"

# Usual update
sudo apt-get -y update
sudo apt-get -y dist-upgrade
sudo apt-get -y install python python-pip
sudo apt-get -y install unzip
sudo pip install beautifulsoup4
#Reminder to change user password
clear
echo "Change the new user password" * 5



