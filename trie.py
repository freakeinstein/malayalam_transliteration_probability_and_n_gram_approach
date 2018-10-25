#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random

def scheme_cleaner():
	inp = open("input.txt")
	out = open("myfile","w")
	s = inp.read()
	s = s.replace(" ","")
	#s = s.replace("=>",":")
	s = s.replace('"',"")
	s = s.replace("[","")
	s = s.replace("]","")
	s = s.replace("(","")
	s = s.replace(")","")
	s = s.replace(",\n","\n")
	s = s.replace("\n\n","")
	out.write(s)
	out.close() # Not perfect, better.

def trie(scheme_file):
	d = dict()
	input = open(scheme_file,"r")
	str = input.read()
	lines = str.split('\n')
	for line in lines:
		#print("+++++++++")
		pair = line.split("=>")
		keys = pair[0].split(",")
		values = pair[1].split(",")
		#print(keys,values)

		value_weight_pair_list = []
		for value in values:
			split = value.split("|")
			value_weight_pair_list.append([split[0],int(split[1])])
		#print("val pair lst: {}".format(value_weight_pair_list),"\n")

		for key in keys:
			new_list = []
			try: 
				new_list = value_weight_pair_list + d[key] # If the key is already present, add new list to the old list
			except KeyError as e:
				new_list = value_weight_pair_list
			finally: 
				d[key] = new_list
				#print(key,new_list)
	return d # Tested OK !

def normalize_trie(dictionary,min,max,start,end):
	"""
	print("normalized from {} - {} to {} - {}".format(min,max,start,end))
	
	"""
	for key in dictionary.keys():
		value = dictionary[key]
		lst = []
		for val in value:
			#print(val)
			sum = mapper(val[1],min,max,start,end)
			lst.append([val[0],sum])
			#print("sum:{}".format(sum))
		dictionary[key] = lst

def mapper(val,min,max,start,end):
	return round(val/(max-min)*(end-start))

def write_random_wt_trie(dictionary,start,end):
	fh = open("snapshot.txt","w")
	s=""
	for dict_pair in sorted(dictionary.items()):
		s = s+dict_pair[0]+"=>"
		for val_list in dict_pair[1]:
			s = s+val_list[0]+"|"+str(random.randint(start, end))+","
		s+="\n"

	fh.write(s)
	fh.close() 

def backup_trie(dictionary):
	fh = open("snapshot.txt","w")
	s=""
	for dict_pair in sorted(dictionary.items()):
		s = s+dict_pair[0]+"=>"
		for val_list in dict_pair[1]:
			s = s+val_list[0]+"|"+str(val_list[1])+","
		s+="\n"
	fh.write(s)
	fh.close() 
