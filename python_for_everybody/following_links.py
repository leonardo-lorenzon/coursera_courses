import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def following_links():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL- ')
    position = int(input('Enter position link - '))
    loop = int(input('Enter number of loops - '))
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    cont = 0
    while cont < loop:
        last_name = tags[position - 1].contents[0]
        new_url = tags[position - 1].get('href', None)
        html = urllib.request.urlopen(new_url, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        cont += 1
    return last_name

print(following_links())
