#!/usr/bin/env python
import csv
import urllib2
import commands
import subprocess
import os;
import sys;
import re;
import csv;
import time;
#Created by:Anthonys.io
#Twitter.com/Tech
with open("cookies.txt") as f:
	for line in f:
		if "_twitter_sess" in line:  
			if "twitter.com" in line:
				if "_twitter_sess" in line:
					getcooks = line.split("_twitter_sess",1)[1]
					fixcooks = getcooks.lstrip().rstrip()
		if "auth_token" in line:  
			if "twitter.com" in line:
				if "auth_token" in line:
					getcooks1 = line.split("auth_token",1)[1]
					fixcook = getcooks1.lstrip().rstrip()
sessid = "_twitter_sess="+fixcooks
auth = "auth_token="+fixcook
print "Enter Your Tweet:",
tweet = raw_input()
curl = ("curl 'https://twitter.com/i/tweet/create' -H 'Host: twitter.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Twitter-Active-User: yes' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: https://twitter.com/' -H 'Cookie: "+sessid+"; remember_checked_on=1\"; "+auth+";' -H 'DNT: 1' -H 'Connection: keep-alive' --data 'is_permalink_page=false&page_context=profile&place_id=&status="+tweet+"&tagged_users=&weighted_character_count=true'")
output = commands.getoutput(curl)
if 'tweet_html' in output:
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    print('\x1b[6;30;42m' + '' + '\x1b[0m')
else:
    print "Error" 
    print output
