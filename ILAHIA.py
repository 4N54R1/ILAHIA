#!/usr/bin/python(Created By Arhaan)
import urllib2
import sys
url = raw_input("Enter Full Url of Target Website")
url.rstrip()
header = urllib2.urlopen(url).info()
print (str(header))
