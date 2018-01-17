from SSK import *
from parse import *
from SubString import *

def main():
    k = 2
    list_of_doc_tuples = init()
    dict_of_features = dict()
    for doc in list_of_doc_tuples:
        dict_of_features = StringParser(k,doc[0], dict_of_features)
    
    subspace_of_features = Convert_to_dict_Array(dict_of_features) 
    result = start_string_kernel(k, docs, subspace_of_features)

main()
