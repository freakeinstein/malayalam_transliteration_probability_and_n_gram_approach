from . import unicode_reader as ur
from . import ml2en
from . import char_split as cs
import trie
import time


def start_scheme_training(dictionary,input_file):
	training_data_ml = ur.read_malayalam(input_file)
	fh = open("temp.txt","w")
	fh.write(training_data_ml)
	fh.close()
	converter = ml2en.ml2en()
	print("transliterating{}".format(time.ctime()))
	s=""
	for word in training_data_ml.split():
		s = s + converter.transliterate(word)+" "
	training_data_en = s
	do_train(dictionary,training_data_ml,training_data_en) #Pass manglish and corresponding malayalam paragraph for matching and training
	#do_normalize_weights(dictionary)
	return dictionary

def do_train(dictionary,training_data_ml,training_data_en):
	print("starts training{}".format(time.ctime()))
	split_data_ml = training_data_ml.split()
	i = -1
	# Get two lists for segmentation from trie (keys list and values list)
	keys_list = get_keys_list(dictionary)
	vals_list = get_vals_list(dictionary)
	for split_data_en in training_data_en.split():
		i+=1
		split_data_en_modified = "_"+split_data_en #Adding a beginning notation
		# Everything is preprocessed from paragraph for one by one words training
		keys_list = group_manglish(split_data_en_modified,keys_list)[0]
		vals_list = group_malayalam(split_data_ml[i],vals_list)[0]
	update_Trie_with_training_values(dictionary,keys_list,vals_list)

def update_Trie_with_training_values(dictionary,keys_list,vals_list):
	#print(dictionary)
	large = 0
	for pair in keys_list:
		#print(pair)
		value = dictionary[pair[0]]
		lst = []
		for val in value:
			sum = 0
			sum = val[1] + pair[1] + get_value_weight(val[0],vals_list)
			lst.append([val[0],sum])
			if sum > large:
				large = sum
		dictionary[pair[0]] = lst
		#if(large > 500):
			#trie.normalize_trie(dictionary,1,large,1,100)
			#large = 0
	#print(dictionary)
	#print(large)
	#trie.normalize_trie(dictionary,1,large,1,100)
	#print(dictionary)

def get_value_weight(val,vals_list):
	for ch in vals_list:
		if id(ch[0]) == id(val):
			return ch[1]
	return 0

def group_manglish(text,lis):
	#lis = [['ാ',0],['യ',0],['ഹ',0]]
	lis = any_text_segment(text,lis)
	remain = lis[1]
	lis = lis[0]
	return [lis,remain]

def group_malayalam(text,lis):
	#lis = [['ാ',0],['യ',0],['ഹ',0]]
	lis = any_text_segment(text,lis)
	remain = lis[1]
	lis = lis[0]
	return [lis,remain]

def any_text_segment(txt,lis): # To segment the string and to count the occurences from a list
	#txt='_'+txt
	found_substring = True
	while txt and found_substring: # Until all the substrings are found
		i = 0
		found_substring = False
		lis.sort(reverse=True)
		for sub in lis:
			ix = txt.find(sub[0])
			if ix != -1 :
				found_substring = True
				txt = txt[:ix]+"+"+txt[ix+len(sub[0]):]
				lis[i][1]+=1
				#print(txt,sub[0],i)
				#print("=",end="")
			i+=1
	return [lis,txt] # return substring count and remaining text
		
def get_keys_list(dictionary):
	lst = []
	for key in dictionary.keys():
		lst.append([key,0])
	return lst

def get_vals_list(dictionary):
	lst = []
	for values in dictionary.values():
		for value in values:
			lst.append([value[0],0])
	return lst
