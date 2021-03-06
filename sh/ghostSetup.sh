#!/bin/bash
# A script to get ghost installed and ready to go
# To download this script
# sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/ghostSetup.sh && chmod 775 ghostSetup.sh


# Set up traps
	TMP="/tmp/$0.1"
	trap "rm -f $TMP; echo 'removing $TMP'" 0 1 2 3 4 5 

#Let the user know what is happening

	echo -e "This script will install Python, Node.Js, Ghost, forever and nginx.\nDo you wish to proceed? [y|n]"
	read ANS
	[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"

# Get the ipaddress for ghost set up
	IPADDRESS=`ip addr show eth0 | grep -e inet | awk '{ print $2; }' | sed 's/\/.*$//' | grep -v ::`
	echo "This is your IP Address: $IPADDRESS"

# Set up a new user with home directory to store ghost install
# Uncomment if necessary

#	echo -e "Creating new user. Enter new user name: "
#	read USERNAME
#	echo -e "Creating new user. Enter new user password: "
#	read PASSWD
#	useradd -m -s /bin/bash -d /home/$USERNAME -U $USERNAME -p $PASSWD
#	sudo usermod -a -G sudo $USERNAME
#	echo "New user created"

# Download ghost dependencies, Ghost and set up some of them from new user home
	mkdir -p /var/www/
	cd /var/www/
# Base updates and installs
	sudo apt-get -y install python-software-properties 
	sudo apt-add-repository ppa:chris-lea/node.js -y
	sudo apt-get -y update
	sudo apt-get -y dist-upgrade
	sudo apt-get -y install nodejs
	sudo npm install forever -g
	sudo apt-get -y install unzip
	sudo wget https://ghost.org/zip/ghost-latest.zip
	sudo unzip -d ghost ghost-latest.zip

# Basic ghost configuration to run on your IP address
# You will need to change it to your domain

	cd ghost/
	sudo cp config.example.js config.js
	GHOSTURL="http\:\/\/my-ghost-blog.com"
	CONFIGIP="http\:\/\/$IPADDRESS"
	ECHO "$CONFIGIP"
	cat config.js | sudo sed -e "s/$GHOSTURL/$CONFIGIP/g" > $TMP
	sudo mv -f $TMP config.js
	clear
	cat config.js
	echo -e "\nIf this config file looks ok.\n!!Check the URL: $IPADDRESS!!\nDo you wish to proceed [y|n]"
	read ANS
	[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
	sudo npm install --production
	cd .. && sudo chown -R www-data:www-data ghost

# Installing nginx and setting it up to host ghost
# again, only on the ipaddress. You will need to configure a domain

	sudo apt-get -y install nginx
	cd /etc/nginx/sites-available
	sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/ghostconf.txt
	sudo mv ghostconf.txt ghost.conf
	IPADD="IPADDRESS_HOLDER"
	sudo sed -i "s/$IPADD/$IPADDRESS/" ghost.conf
	clear
	cat ghost.conf
	echo -e "\n If this config file looks ok.\n!!Check the IP Address: $IPADDRESS!!\nDo you wish to proceed [y|n]"
	read ANS
	[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
	sudo ln -s /etc/nginx/sites-available/ghost.conf /etc/nginx/sites-enabled/ghost.conf	
	sudo rm /etc/nginx/sites-enabled/default

# Start ghost with the forever command & nginx	

	cd /var/www/ghost
	STARTGHOST="NODE_ENV=production forever start index.js"
	sudo $STARTGHOST
	sudo service nginx restart
	cd ~ && rm -rf tmp
	clear
	echo -e "Ghost, nginx, and nodejs are installed"
	echo -e "You need to configure them now"
	echo -e "To test this install, type your IP Address into a browser\n$IPADDRESS"