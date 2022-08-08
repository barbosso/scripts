#!/bin/bash

boxName=$1;
IP=$2;
dir=$1-$2;
rootdir=$HOME/htb/;

function empty {
	if [[ $(echo $1 | wc -m) == 1 ]]; then
		echo "Usage: ./newHTB.sh [boxname] [IP address]";
		exit;
	fi
}

function dirCheck {
	if [ -d $1 ]; then
		mkdir -p $rootdir;
	fi
}

empty "$boxName";
empty "$IP";
dirCheck "$rootdir";
cd $rootdir;
mkdir $dir;
cd $dir
echo "$IP $boxName" | xclip -sel clip;
sudo nano /etc/hosts;
echo "[+] Starting Masscan and Nmap scan..";

sudo masscan -e tun0 -p1-65535,U:1-65535 $IP --rate=500 | grep Discovered | awk '{print $4}' | cut -d/ -f1 > ports;

sudo nmap -Pn -sV -sC -sN -p $(tr '\n' , < ports) -T4 -v $IP -oN $IP.nmap;

if [[ $(curl -Is http://$boxName.htb | grep HTTP/1.1 | awk {'print $2'}) == 200 ]]; then
	echo "[+] Starting simple dirb scan";
	dirb http://$boxName.htb > dirb.out;
else
	echo "[+] $IP doesn't seem to have a webserver on port 80";
fi