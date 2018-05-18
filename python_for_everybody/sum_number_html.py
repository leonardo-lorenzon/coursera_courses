import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def sum_number_url(url):

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    total_sum = 0
    span_tags = soup('span')
    for num in span_tags:
        total_sum += int(num.contents[0])
    return total_sum



if __name__ == '__main__':
    url = input('Enter - ')
    print(sum_number_url(url))
