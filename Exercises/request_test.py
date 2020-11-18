import re
import requests

url_1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
url_3 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_4 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
url_5 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
url_6 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


def find_urls(url, template=r'<a[^>]*?href=[\"|\'](.*?)[\"|\'][^>]*?>'):
    """ search all links to next pages """
    response = requests.get(url).text
    urls = re.findall(template, response)
    return urls


def main(url_a, url_b):
    """ checking that we can get to url_b from url_a after two transition """
    urls = []
    for url in find_urls(url_a):
        urls += find_urls(url)
        if url_b in urls:
            return 'Yes'
    return 'No'


assert main(url_1, url_2) == 'Yes'
assert main(url_3, url_4) == 'No'
assert main(url_5, url_6) == 'Yes'
