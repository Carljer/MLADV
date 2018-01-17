import string
import itertools

def main(n = 1, dataset = ""):
	
	alphabet = string.ascii_lowercase[:] + " "

	allsub_couter = dict()

	#print(alphabet)

	allsub = get_all_substrings(alphabet,n)

	for i in range(len(allsub)):

		allsub_couter[allsub[i]] = 0

	#dicten med data i
	print(freequency(allsub_couter,dataset,n))
	#freequency(allsub_couter,dataset,n)

def get_all_substrings(S,n):

	return ["".join(x) for x in itertools.product( S, repeat=n)]

def freequency(allsub_couter, dataset, n):

	for x in range(len(dataset)-(n-1)):
		allsub_couter[dataset[x:x+n]] = allsub_couter[dataset[x:x+n]]+ 1






	return allsub_couter 

if __name__ == '__main__':
	main(2, "hej jag heter")
