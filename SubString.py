import string
import itertools


#Main loopen för att skapa featurespace
def StringParser(n = 1, dataset = "", allsub_couter = dict(), flag = True):
    
    alphabet = string.ascii_lowercase[:] + " "
    allsub = get_all_substrings(alphabet,n)

    for i in range(len(allsub)):

        allsub_couter[allsub[i]] = 0

    #dicten med data i
    return freequency(allsub_couter,clean_Stirng(dataset),n)

#skapar alla möjliga substrings av storlek n av alfabet S
def get_all_substrings(S,n):

    return ["".join(x) for x in itertools.product( S, repeat=n)]

#Beräkar antalet förekommster av de olika substrängarna i Datasetet
def freequency(allsub_couter, dataset, n):

    for x in range(len(dataset)-(n-1)):
        allsub_couter[dataset[x:x+n]] = allsub_couter[dataset[x:x+n]]+ 1

    return allsub_couter 


#Tar bort otillåtna tecken och tar bort versaler (gör dem till gemener) 
def clean_Stirng(string):

    naughtyString = "!€%&#/()=^*¨><.,;:"

    gemen = string.lower()
    
    for char in naughtyString:
        #print(char)
        gemen = gemen.replace(str(char), "")

    clean_string = gemen
    return clean_string

def Convert_dict_to_Array(dict,flag = True):
    dictlist = []

    if flag:
        for key, value in dict.items():
            if (value > 2):
                dictlist.append(key)
        return dictlist

    if not flag:
        for key, value in dict.items():
            if (value >= 0):
                dictlist.append(key)
        return dictlist


# if __name__ == '__main__':
#     x = StringParser(3, "HEJ hehehhehehehehe jag #RA,,.;; heter", dict(),False)
#     print(Convert_dict_to_Array(x,False))
