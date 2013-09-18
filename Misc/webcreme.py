# Webcreme website design inspiration
# It opens a random website from http://www.webcreme.com/
# It saves all visited websites in a text file

from bs4 import BeautifulSoup
import urllib
import webbrowser
import re
import random

def get_number_pages():
    page = urllib.urlopen("http://www.webcreme.com/").read()
    soup = BeautifulSoup(page)
    pages = soup.find('div', class_='navigation').contents[0]

    regex = re.search('(\d+)', pages)
    return regex.group(1)


def get_url_from_page(page):
    page = urllib.urlopen("".join(["http://www.webcreme.com/page/", page])).read()
    soup = BeautifulSoup(page)

    websites = soup.find_all('div', class_='image')

    while True:
        # bug: if all websites of this page have been visited it enters an infinite loop
        chosen_one = random.randrange(len(websites))
        url = websites[chosen_one].a['href']

        if not visited_before(url):
            return (chosen_one, websites[chosen_one].a['href'])


def save_url(url):
    with open("visited.txt", "a") as f:
        f.write("".join([url, "\n"]))


def visited_before(url):
    with open("visited.txt", "r") as f:
        for visited_url in f:
            if visited_url.strip() == url:
                return True
        return False


def main():
    pages = get_number_pages()
    page = random.randint(1, int(pages))

    url = get_url_from_page(str(page))
    webbrowser.open_new(url[1])
    save_url(url[1])

    print "Opening '{2}', page {0}, link #{1}".format(page, url[0]+1, url[1])

if __name__ == "__main__":
    main()
