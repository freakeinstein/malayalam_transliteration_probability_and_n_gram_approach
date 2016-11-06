#! /usr/bin/python3
# -*- coding: utf-8 -*-

import spellchecker

def perform_final_spell_check(word):
	instance = spellchecker.getInstance()
	return instance.suggest(word,distance=1) if not instance.check(word) else [word]