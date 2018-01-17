from SSK import *
from parse import *
from SubString import *

def main():
    k = 2
    list_of_doc_tuples = init()
    dict_of_features = dict()
    for doc in list_of_doc_tuples:
        dict_of_features = StringParser(k,doc[0], dict_of_features)
    
    subspace_of_features = Convert_dict_to_Array(dict_of_features)
    docs = []
    for tup in list_of_doc_tuples:
        docs.append(tup[0])
    result = start_string_kernel(k, list_of_doc_tuples, subspace_of_features)
    print(result)

main()
