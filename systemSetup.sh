#!/bin/bash

# A script to update a new VM to my usual needs
# To download this script
# wget -c https://github.com/zaniphrom/bash/blob/master/systemSetup.sh && chmod 775 systemSetup.sh
 

echo "just print as test"
echo -e "enter the user pw\n:> "
read PASSWD
  

# Usual update
sudo apt-get -y update
sudo apt-get -y dist-upgrade
sudo apt-get -y install python python-pip
sudo apt-get -y install beautifulsoup4


# make new user with sudo rights and home directory

useradd -m -s /bin/bash -d /home/brian -U brian -p $PASSWD



