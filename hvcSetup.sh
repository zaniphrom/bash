#!/bin/bash
#A script to get HVC mining quickly
#sudo wget -c https://raw.githubusercontent.com/zaniphrom/bash/master/hvcSetup.sh && chmod 775 hvcSetup.sh
echo -e "This script will install, set up and run a heavycoin mine.\n do you wish to proceed [y|n]"
read ANS
[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
sudo dd if=/dev/zero of=/swapfile bs=64M count=16 
sudo mkswap /swapfile
sudo swapon /swapfile
sudo apt-get -y update
sudo apt-get -y dist-upgrade
sudo apt-get -y install automake build-essential libcurl4-openssl-dev git zip
git clone https://github.com/heavycoin/cpuminer-heavycoin
cd cpuminer-heavycoin
sudo sed -i 's/@LIBCURL@ @JANSSON_LIBS@ @PTHREAD_LIBS@ @WS2_LIBS@ -lssl/@LIBCURL@ @JANSSON_LIBS@ @PTHREAD_LIBS@ @WS2_LIBS@ -lssl -lcrypto/' Makefile.am
chmod a+x autogen.sh
./autogen.sh
./configure CFLAGS="-O3"
make
echo -e "Enter your wallet address pw\n:> "
read WALLET
echo "you will mine to $WALLET"
echo -e "\n do you wish to proceed [y|n]"
read ANS
[ $ANS == "n" ] && echo "exiting....." && sleep 1 && exit 0 || echo "programme running"
nohup ./minerd -a heavy -v 512 -o stratum+tcp://hvcpool.1gh.com:5333 -u $WALLET -p heavymine & 
echo "HeavyCoin now mining. See your progress with 'cat nohup.out | grep -ie yay"