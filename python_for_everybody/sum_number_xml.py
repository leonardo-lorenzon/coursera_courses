import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

def get_xml_data(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    xml = urllib.request.urlopen(url, context = ctx).read()
    return xml

def sum_number_xml(url):
    total_sum = 0
    xml = get_xml_data(url)

    tree = ET.fromstring(xml)
    comment_list = tree.findall('comments/comment')

    for item in comment_list:
        total_sum += int(item.find('count').text)
    return total_sum

if __name__ == '__main__':
    url = input('Enter URL - ')
    print(sum_number_xml(url))
