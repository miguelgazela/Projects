#!usr/bin/env python

# Get Atomic Time from Internet Clock
# This program will get the true atomic time from an atomic time clock on the
# Internet. There are various clocks across the world. 
# Do a search for a list of them.

import urllib2
from bs4 import BeautifulSoup

def main():
    content = urllib2.urlopen("http://time.is/")
    page = BeautifulSoup(content)

    time = page.find(id="twd").string
    location = page.find("h1", id="pL").a.string

    print "It's currently {0} in {1}.".format(time, location)

if __name__ == "__main__":
    main()

