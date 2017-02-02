#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Configuration:
    
    _instance           = None
    
    file_training_url   = "data/beach.csv"              # default file to training set
    file_examples_url   = "data/examples.csv"           # default file with test set
    file_output_url     = "data/output.csv"
    file_depurated_url  = "data/beach_depurated.csv"    # file with the depurated files 
                                                        #   to be used at pruning
    splitter            = ","                           # comma is the default split caracter
    unknown_values      = ['','-','?']                  # values that describe a empty value
    min_error           = 1.0                           # error min to use on pruning
    print_tabs_num      = 0                             # size of tab on print tree
    num_split_columns   = 1                             # number of columns removed from left
                                                        #   0 don't remove any collumn
                                                        #   1 remove the first
                                                        #   2 remove the first e secound collumns...
    slicer_percentage   = 0.6
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
        return cls._instance

	def __init__(self):
		self.file_url         = "data/beach.csv"
		self.splitter         = ","               
        self.unknown_values   = ['','-','?']        
        self.print_tabs_num   = 0
        self.num_split_columns= 1 

	# Method used to print the configuration
	#	used on configuration
	def printConfiguration(self):
		print "Property           | Value"
		print " File url             ",self.file_url
		print " Unknown Values	     ",self.unknown_values
        print " Print tabs num	     ",self.print_tabs_num
        print " Num split columns	 ",self.num_split_columns