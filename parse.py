from bs4 import BeautifulSoup
from lxml import etree

DIR = "reuters21578"

def read_document(filename):
    with open(DIR + '/' + filename, 'r') as sgm_file:
        soup = BeautifulSoup(sgm_file, 'html.parser')
        earn_counter = 0
        for content in soup.find_all(lewissplit="TRAIN"):
            for category in content.find_all('topics'):
                if category.get_text() == 'earn':
                    earn_counter += 1

        print(earn_counter)

def init():
    document = 'reut2-014.sgm'
    train = read_document(document)
    # parsed_doc = read_document(document)
    # for docs in parsed_doc:
    #     print(docs)


