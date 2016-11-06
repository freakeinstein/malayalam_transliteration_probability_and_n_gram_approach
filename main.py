#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import stemmer
import retrieve_from_trie as rft
import trie
from train import language_training as l_train
from train2 import bigram_training as bgt
import bigram_sort as bgs
import final_spell_checks as fsc
from mlphone import MLphone
import symspell_python

from train import ml2en # for test() method
import random

arginp = sys.argv[1]
argcount = int(sys.argv[2])

def main():
	language_trie = trie.trie("input.txt") # To load trie from scheme file. clean code. tested
	level_2_list = get_finalized_suggestion(language_trie,arginp,argcount,"bigram_mal_corpus.txt")
	#training_phase()
	#test(language_trie,"malayalam.txt",module1=True)
	symspell_python.create_dictionary("malayalam.txt")
	#print(symspell_python.dictionary)
	for ii in level_2_list:
		##print(mlphone_calculator(ii[0]))
		print(symspell_python.get_suggestions(ii[0]))



def get_finalized_suggestion(language_trie,input_mangleesh,suggestion_limit,bigram_corpus_file):
	level_1_list = get_level1_suggestions(language_trie,input_mangleesh,suggestion_limit)
	level_2_list = bgs.bigram_sort(level_1_list,bigram_corpus_file)
	#print(level_2_list)
	#print("===================================================")
	#for suggestion in level_2_list: # spell checking seems to be useless here.
		#print(k,v)
		#print("suggestion: ",end="")
		#for iii in fsc.perform_final_spell_check(suggestion[0]):
			#print(iii)
	return level_2_list

def training_phase(scheme_train = False, persistance = False, bigram_train = False):
	if scheme_train:
		language_trie = l_train.start_scheme_training(language_trie,"malayalam.txt")
	if persistance:
		trie.backup_trie(language_trie)
	if bigram_train:
		bgt.start_bigram_training("malayalam.txt","bigram_mal_corpus.txt")

def test(language_trie,input,module1 = False,module2 = False,module3 = False):
	if module1:
		test_accuracy_module_1(language_trie,input)
	if module2:
		pass
	if module3:
		pass

def test_accuracy_module_1(language_trie,input):
	fin = open(input)
	str = fin.read()
	str_split = str.split("\n")
	count = len(str_split) - 1
	i = 0
	c=10000
	per = 0
	test_module_2_pipe = list()
	converter = ml2en.ml2en()
	while i<c:
		#print("|",end="")
		i+=1
		ran = random.randint(0,count)
		arginp1 = converter.transliterate(str_split[ran].split(" ")[0])
		level_1_list = get_level1_suggestions(language_trie,arginp1,argcount)
		#print(level_1_list)
		#test_module_2_pipe.append(level_1_list)
		try:
			if len(str_split[ran].split(" ")[0]) == len(level_1_list[0][0]) :
				per += 1
		except:
			pass
	print(per,per/100)


def get_level1_suggestions(language_trie,arginp,argcount):
	gen = rft.base_trans(language_trie,arginp)
	lst = []
	for i in range(argcount):
		try:
			#stemmer.mystem(next(gen))
			lst.append(next(gen))
		except:
			continue
	return lst

def mlphone_calculator(ml_str):
	converter = MLphone()
	return converter.compute(ml_str)

if __name__ == "__main__": main()