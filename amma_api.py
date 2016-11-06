import trie
import main
from train import unicode_reader as ur
from train import language_training as lt

#from mlphone import MLphone

def amma_api_initiate_trie():
	return trie.trie("input.txt") # To load trie from scheme file. clean code. tested

def amma_api_initiate_spell_dictionary(sp):
	sp.create_dictionary(speed=50,segment=50000)

def amma_api_suggest_word(language_trie,input_mangleesh,sp,efficiancy=5):
	level_2_list = main.get_finalized_suggestion(language_trie,input_mangleesh,efficiancy,"bigram_mal_corpus.txt")
	#print(level_2_list)
	lst1 = list()
	for item in level_2_list:
		spell_corrected_list = sp.get_suggestions(item[0],silent=True)
		if(spell_corrected_list):
			#print(spell_corrected_list)
			for spell in spell_corrected_list:
				lst1.append(spell)
	return lst1

def teach_with_new_pair(sp,dictionary,malayalam,mangleesh):
	print("starts user training")
	print(malayalam)
	sp.create_dictionary_entry(malayalam) # to add neww text into the spell checker dictionary
	sp.add_to_db(malayalam) #not ready
	lt.do_train(dictionary,malayalam,mangleesh) # to train module 1 language trie
	#module 2 training is indetermined on how to do it
	print("training succeeded !")


