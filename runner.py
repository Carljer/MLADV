from SSK import *
from parse import *
from SubString import *

def main():
    k = 2
    list_of_doc_tuples = init()
    reduced_feature_space = False
    dict_of_features = dict()
    for doc in list_of_doc_tuples:
        dict_of_features = StringParser(k,doc[0], dict_of_features)
    
    subspace_of_features = Convert_dict_to_Array(dict_of_features, reduced_feature_space)
    docs = []
    for tup in list_of_doc_tuples:
        docs.append(tup[0])
    
    result_list = []
    for i in range(10):
        result_list.append(start_string_kernel(k, list_of_doc_tuples, subspace_of_features))
    
    df = pd.DataFrame(result_list)
#     df.columns(['ssk precision','ssk recall','ng precision','ng recall'])
    print(df)
    print('means', df.mean(axis=0))
    print('std', df.std(axis=0))
main()
