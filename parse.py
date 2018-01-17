from bs4 import BeautifulSoup
from lxml import etree
import re

DIR = "reuters21578"

def read_document(filename):
    with open(DIR + '/' + filename, 'r') as sgm_file:
        soup = BeautifulSoup(sgm_file, 'html.parser')
        earn_counter = 0
        result = []
        for content in soup.find_all('reuters'):
            for body in content.find_all('body'):
                b = body.get_text().lower()
                b = ''.join([i for i in b if not i.isdigit()])
                category = content.find('topics').get_text()
                if category == 'earn':
                    result.append((re.sub(r'\W+', ' ', b), category))
                if category == 'acq':
                    result.append((re.sub(r'\W+', ' ', b), category))
        return result


def init():
    document = 'reut2-014.sgm'
    data = read_document(document)
    return data


init()
