#!/usr/bin/python

import urllib

target = raw_input("Enter URL Site : ")

list = ['admin','users','online','MyAdmin','backend','cms','sysadmin','wp-admin','administrator','CMS','crm','login']

for l in list:
    url = target +"/"+l
    response = urllib.urlopen(url)
    print url
    if (response.code == 200):
        print ("Sucses")
        break

