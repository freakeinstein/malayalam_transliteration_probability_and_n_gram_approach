#! /usr/bin/python3
# -*- coding: utf-8 -*-

from indicsyllabifier import getInstance

def split_malayalam_chars(mal_str):
	instance = getInstance()
	return instance.syllabify(mal_str)
