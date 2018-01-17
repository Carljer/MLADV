from SSK import *
from parse import *

def main():
    k = 2
    list_of_docs = init()
    dict_of_features = dict()
    for doc in len(list_of_docs):
        dict_of_features = StringParser(k,doc, dict_of_features)
    
    subspace_of_features = Convert_to_dict_Array(dict_of_features) 
    result = start_string_kernel(k, docs, subspace_of_features)

main()