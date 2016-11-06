#!usr/bin/python3
# -*- coding: utf-8 -*-

from train import unicode_reader as ur
import indicngram
import operator
import time

# To train and generate a bigram corpus ( nothing to do with sggestions, this is independent file generation only)

def start_bigram_training(input_file,output_file):
	fh=open(output_file,"w")
	print("Begin: {}".format(time.ctime()))
	x=learn_bigram(input_file)
	print("Learning complete, sorting: {}".format(time.ctime()))
	malayalam_bigram_table = list(sorted(x.items(), key=operator.itemgetter(1), reverse= True))
	#malayalam_bigram_table.sort()
	s=" Bigram malayalam corpus | JUBIN JOSE #"+str(malayalam_bigram_table[0][1])
	for i in malayalam_bigram_table:
		s=s+"\n"+i[0]+":"+str(i[1])
	fh.write(s)
	fh.close()
	print("End [{} combinations found.]: {}".format(len(malayalam_bigram_table),time.ctime()))
	
def learn_bigram(input_file):
	print("Read file: {}".format(time.ctime()))
	dictionary = dict()
	s = ur.read_malayalam(input_file)
	print("Starts learning: {}".format(time.ctime()))
	for word in s.split():
		bigram = generate_bigram('_'+word+'_')
		for key in bigram:
			try:
				dictionary[key] += 1
			except:
				dictionary[key] = 1
	return dictionary

def generate_bigram(word):
	ngram_instance = indicngram.getInstance()
	return ngram_instance.letterNgram(word)


if __name__ == "__main__": main()

