#! /usr/bin/python3
# -*- coding: utf-8 -*-

from train2 import bigram_training as bgt
import indicngram

# to sort suggestions based on bigram thats already generated.

def bigram_sort(level_1_list,input):
	bigram_scheme = dict()	
	fh = open(input,"r")
	s = fh.readline()
	s = fh.read()
	for line in s.split("\n"): ## To create a RAM snapshot of bigram already learned data from file (bigram corpus)
		spl = line.split(":")
		try:
			existing = list()
			new = list()
			key = spl[0]
			existing = bigram_scheme[key[0]]
			existing.append([key[1],spl[1]])
			bigram_scheme[key[0]] = existing
		except:
			bigram_scheme[spl[0][0]] = [[spl[0][1],spl[1]]]

	result = dict()
	
	#for rr in sorted(bigram_scheme.items()):
	#	print(1/len(rr[1]),rr,"\n\n")

	level_2_list = list()
	for pair in level_1_list: ## for each suggestions, split it into bigrams and compute its bigram sum
		bigram_list = generate_bigram(pair[0])
		prob = 1
		for bigram in bigram_list:
			next_gram_list = bigram_scheme[bigram[0]]
			length_of_next_gram_list = len(next_gram_list)
			prob_per_gram = 1/length_of_next_gram_list
			#print(prob_per_gram,length_of_next_gram_list)

			if bigram[1] in get_list_from_bigrams_list(next_gram_list):
				#print("{} prob: {} * {} = {}".format(bigram,prob,prob_per_gram,prob * prob_per_gram))
				prob *= prob_per_gram
			else:
				prob *= 0
				#print("___{}____".format(bigram))
		#print([pair[0],pair[1],pair[1]*prob])
		level_2_list.append([pair[0],pair[1]*prob])
		level_2_list = sort_suggested_result(level_2_list)
	return level_2_list

def sort_suggested_result(lst):
	lst.sort(key = lambda row: row[1],reverse=True)
	return lst # Tested Ok ! # Tested Ok !

def get_list_from_bigrams_list(b_list):
	lst = list()
	for item in b_list:
		lst.append(item[0])
	return lst

def generate_bigram(word):
	ngram_instance = indicngram.getInstance()
	return ngram_instance.letterNgram(word)