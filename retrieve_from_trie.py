#! /usr/bin/python3
# -*- coding: utf-8 -*-

import itertools

def base_trans(dictionary,arginp):
	#scheme_cleaner()
	#for i in sort_suggested_result(dictionary,sys.argv[1]): 
		#print(i[0])
	#print(filter_key_string(dictionary,sys.argv[1]))
	#print(sort_suggested_result(dictionary,sys.argv[1]))
	#print(parse_malayalam_letters(dictionary,'_'+arginp))
	#print(make_suggestion_list_from_combinations(parse_malayalam_letters(dictionary,'_'+arginp)))
	suggestion_back_list = probablize_suggestions(make_suggestion_list_from_combinations(parse_malayalam_letters(dictionary,'_'+arginp)))
	#print("prrr: {}".format(suggestion_back_list))
	return make_suggestion_text_pygenerator(suggestion_back_list)
	
	#write_trie(dictionary)
	


# Methods to generate malayalam words from mangleesh (Process order from bottom to top | top to bottom calling order)

def make_suggestion_text_pygenerator(suggestion_back_list):
	for tupl in suggestion_back_list:
		yield ["".join(tupl[0]),tupl[1]]

def probablize_suggestions(mixer_out):
	#print(mixer_out)
	word_wt_pair_list = []
	for word_wt_pair in mixer_out:
		mult_prob_of_word = 1
		word = []
		for char_wt_pair in word_wt_pair:
			mult_prob_of_word *= char_wt_pair[1]
			word.append(char_wt_pair[0])
		word_wt_pair_list.append([word,mult_prob_of_word])
	return word_wt_pair_list	

def make_suggestion_list_from_combinations(mixer_in):
	return list(itertools.product(*mixer_in))

def parse_malayalam_letters(dictionary,mal_word):
	eng="" 
	mal=[]
	for i in mal_word:
		#print(eng+i)
		suggestions=sort_suggested_result(dictionary,eng+i)
		#print(suggestions)
		if len(suggestions) > 0:
			eng += i
		else:
			if eng == '_' : 
				eng=i
				continue

			temp_pair=[]
			for ml in sort_suggested_result(dictionary,eng):
				temp_pair.append(ml)
			temp_pair = unique_list_ordered(temp_pair) # To make the list unique without repetition
			mal.append(temp_pair)
			#print("\n===== [LOG: (retrieve_from_trie  --  parse_malayalam_letters)]====== \n{}".format(temp_pair))
			eng=i
	temp_pair=[]
	for ml in sort_suggested_result(dictionary,eng):
		temp_pair.append(ml)
	temp_pair = unique_list_ordered(temp_pair) # To make the list unique without repetition
	mal.append(temp_pair)
	#print("\n===== [LOG: (retrieve_from_trie  --  parse_malayalam_letters)]====== \n{}".format(temp_pair))
	#print("\n===== XXXXX [LOG: (retrieve_from_trie  --  parse_malayalam_letters)]====== \n{}".format(mal))
	mal = make_probability_category_list(mal)
	return mal # Not perfect ! just works.. thats all. (To do: add trailing _ as well)

def sort_suggested_result(dictionary,filter_str):
	#print("filter str: {}".format(filter_str))
	result = filter_key_string(dictionary,filter_str)
	custom_result = []
	for pairs in result:
		for value in pairs[1]:
			custom_result.append(value)
	custom_result.sort(key = lambda row: row[1],reverse=True)
	return custom_result # Tested Ok ! # Tested Ok !

def filter_key_string(dictionary,filter_str): # Tested Ok !
	suggestions=[]
	for k , v in sorted(dictionary.items()): 
		suggestions.append([k,v]) if k.startswith(filter_str) else print("",end="")
	#print("\n===== [LOG: (retrieve_from_trie  --  filter_key_string)]====== \n{}".format(suggestions))
	return suggestions # Tested Ok !
	

def unique_list_ordered(seq): #make the list unique by preserving order
	# Order preserving
	''' Modified version of Dave Kirby solution '''
	seen = set()
	return [x for x in seq if x[0] not in seen and not seen.add(x[0])]	

def unique_list_fast(seq): # Not order preserving
  return list(set(seq))

def make_probability_category_list(lst_of_groups):
	plst = []
	for group in lst_of_groups:
		sum = 0
		for pair in group:
			sum += pair[1]
		temp = []
		for pair in group:
			prob = pair[1]/sum
			temp.append([pair[0],prob])
		plst.append(temp)
	return plst
