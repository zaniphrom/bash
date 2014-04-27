#!/bin/bash
# A script to get ghost installed and ready to go
# To download this script
# sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/ghostSetup.sh && chmod 775 ghostSetup.sh
echo -e "This script will install Python, Node.Js, Ghost and nginx.\n Do you wish to proceed? [y|n]"
read ANS
[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
echo -e "Creating new user. Enter new user name: "
read USERNAME
echo -e "Creating new user. Enter new user password: "
read PASSWD
useradd -m -s /bin/bash -d /home/$USERNAME -U $USERNAME -p $PASSWD
sudo usermod -a -G sudo $USERNAME
echo "User created"
cd /home/$USERNAME
# Base updates and installs
sudo apt-get -y install python-software-properties 
sudo apt-add-repository ppa:chris-lea/node.js
sudo apt-get -y update
sudo apt-get -y dist-upgrade
sudo apt-get -y install nodejs
sudo npm install forever -g
sudo apt-get -y install unzip
sudo wget https://ghost.org/zip/ghost-latest.zip
sudo unzip -d ghost ghost-latest.zip
cd ghost/
sudo npm install --production
sudo apt-get -y nginx
sudo apt-get -y somethin
sudo pip install beautifulsoup4
clear
