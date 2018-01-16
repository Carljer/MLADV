from bs4 import BeautifulSoup
from lxml import etree

DIR = "reuters21578"


def read_document(filename):
    with open(DIR + '/' + filename, 'r') as sgm_file:
        soup = BeautifulSoup(sgm_file, 'html.parser')
        bodies = [body for body in soup.find_all('body')]
        return bodies
        

def main():
    documents = ['reut2-002.sgm', 'reut2-002.sgm', 'reut2-002.sgm']
    parsed_docs = []
    for document in documents:
        parsed_docs.append(read_document(document))

    print(parsed_docs)


if __name__ == '__main__':
    main()
