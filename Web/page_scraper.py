from bs4 import BeautifulSoup
import urllib2

def main():
    url = raw_input('URL: ')
    choice = input('Scrape what?\n  1 - Links\n  2 - Images\n  3 - Both\nOption: ')

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    if choice == 1 or choice == 3:
        urls = [link.get('href') for link in soup.find_all('a')]
        print "\n".join(urls)
    if choice == 2 or choice == 3:
        images = [image['src'] for image in soup.find_all('img')]
        print images


if __name__ == "__main__":
    main()