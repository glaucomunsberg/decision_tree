#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from Configuration import *
from ID3 import *
from C45 import *

if __name__ == "__main__":
    
    config  = Configuration()
    
    # read the argv to get commands
    commands = sys.argv[1:len(sys.argv)]
    for i in range(len(commands)):
        commands[i] = commands[i].lower()
        
    if '-i' in commands:
        t_index = commands.index('-i')
        config.file_examples_url = commands[t_index+1]
        
    if '-o' in commands:
        t_index = commands.index('-o')
        config.file_output_url  = commands[t_index+1]
        
    if '-t' in commands:
        t_index = commands.index('-t')
        config.file_training_url = commands[t_index+1]
    
    if '-c45p' in commands and '-d' in commands:
            d_index = commands.index('-d')
            config.file_depurated_url = commands[t_index+1]
    
    file_out = open(config.file_output_url, 'w')
    file_out.truncate()
    
    print('-' * 30)
    
    # Show the file content
    with open(config.file_training_url) as file:
        print("File '"+file.name+"':\n\n{}\n\n" .format("".join(file.readlines())))
    
    # Create the id3 tree, print 
    # and categorize a exemple
    if '-id3' in commands:
        print 'ID3'
        print('-' * 30)
        id3 = ID3(config.file_training_url)
        id3.constructor()
        id3.print_tree()
        # Test exemples from file_examples and 
        #   write at file_out
        with open(config.file_examples_url) as f:
            lines = f.readlines()
            for line in lines:
                row = line.lower().strip().split(config.splitter)
                exemple = Exemple(id3.attributs.list_attributs,row)
                id3.categorize(exemple)
                print("\nlabeled as : '{}'\n".format(exemple.label))
                file_out.write(exemple.label)
                file_out.write('\n')
        
    
    # Create the C45 tree, print 
    # and categorize a exemple
    if '-c45' in commands:
        print '\nC45'
        print('-' * 30)
        c45 = C45(config.file_training_url)
        c45.constructor()
        c45.print_tree()
        # Test exemples from file_examples and 
        #   write at file_out
        with open(config.file_examples_url) as f:
            lines = f.readlines()
            for line in lines:
                row = line.lower().strip().split(config.splitter)
                exemple = Exemple(id3.attributs.list_attributs,row)
                id3.categorize(exemple)
                print("\nlabeled as : '{}'\n".format(exemple.label))
                file_out.write(exemple.label)
                file_out.write('\n')
                
        print('-' * 30)
    
    # Pruning the C45
    if '-c45p' in commands:
        print("C45 - Pruning")
        c45 = C45(config.file_training_url,config.file_depurated_url)
        c45.constructor()
        c45.pruning()
        c45.print_tree()
        # Test exemples from file_examples and 
        #   write at file_out 
        with open(config.file_examples_url) as f:
            lines = f.readlines()
            for line in lines:
                row = line.lower().strip().split(config.splitter)
                exemple = Exemple(id3.attributs.list_attributs,row)
                id3.categorize(exemple)
                print("\nlabeled as : '{}'\n".format(exemple.label))
                file_out.write(exemple.label)
                file_out.write('\n')  

        print('-' * 30)
        
    file_out.close()
