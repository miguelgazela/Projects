import urllib
import sys


def find_country(ip):
    sock = urllib.urlopen("http://whatismyipaddress.com/ip/"+ip)
    html_source = sock.read()

    print html_source

    close sock
    return "Testing"


def main():
    for arg in sys.argv[1:]:
        print "%s - %s" % (arg, find_country(arg))


if __name__ == "__main__":
    main()
