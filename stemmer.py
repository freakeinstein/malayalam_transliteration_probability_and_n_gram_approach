#! /usr/bin/python3
# -*- coding: utf-8 -*-


from indicstemmer import getInstance

def mystem(val):
	instance = getInstance()
	print(instance.stem(val))