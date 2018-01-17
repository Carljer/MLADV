from bs4 import BeautifulSoup
from lxml import etree

DIR = "reuters21578"


def read_document(filename):
    with open(DIR + '/' + filename, 'r') as sgm_file:
        soup = BeautifulSoup(sgm_file, 'html.parser')
        nr_of_doc = 100
        bodies = []
        for body in soup.find_all('body'):
            bodies.append(str(body.get_text()).lower())
            nr_of_doc -= 1
            if nr_of_doc == 0: break
        return bodies


def main():
    document = 'reut2-000.sgm'
    parsed_doc = read_document(document)
    for docs in parsed_doc:
        print(docs)


if __name__ == '__main__':
    main()
