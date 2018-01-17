import string
import itertools

# dic = dict()
# for i in range k:
#     dic = StringParser(1, data, dic)

def StringParser(n = 1, dataset = "", allsub_couter = dict()):
    
    alphabet = string.ascii_lowercase[:] + " "

    #allsub_couter = dict()

    #print(alphabet)

    allsub = get_all_substrings(alphabet,n)

    for i in range(len(allsub)):

        allsub_couter[allsub[i]] = 0

    #dicten med data i
    return freequency(allsub_couter,clean_Stirng(dataset),n)
    #print(clean_Stirng(dataset))

def get_all_substrings(S,n):

    return ["".join(x) for x in itertools.product( S, repeat=n)]

def freequency(allsub_couter, dataset, n):

    for x in range(len(dataset)-(n-1)):
        allsub_couter[dataset[x:x+n]] = allsub_couter[dataset[x:x+n]]+ 1

    return allsub_couter 



def clean_Stirng(string):

    naughtyString = "!€%&#/()=^*¨><.,;:"

    gemen = string.lower()
    
    for char in naughtyString:
        #print(char)
        gemen = gemen.replace(str(char), "")

    clean_string = gemen
    return clean_string

def Convert_dict_to_Array(dict):
    dictlist = []

    for key, value in dict.items():
        if (value > 2):
            dictlist.append(key)
    return dictlist


if __name__ == '__main__':
    x = StringParser(3, "HEJ hehehhehehehehe jag #RA,,.;; heter", dict())
    print(Convert_dict_to_Array(x))
