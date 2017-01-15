#!/usr/bin/python
# -*- coding: utf-8 -*-

from Configuration import *
from ID3 import *
from C45 import *

if __name__ == "__main__":
    
    config  = Configuration()
    
    print('-' * 30)
    
    # Show the file content
    with open(config.file_training_url) as file:
        print("File '"+file.name+"':\n\n{}\n\n" .format("".join(file.readlines())))
      
    # Create the id3 tree, print 
    # and categorize a exemple
    print 'ID3'
    print('-' * 30)
    id3 = ID3(config.file_training_url)
    id3.constructor()
    id3.print_tree()
    exemple = Exemple(["outlook", "temperature", "humidity", "wind"],
                      ["sunny",   "cool",        "High",   "strong"])
    id3.categorize(exemple)
    print("\nlabeled as : '{}'\n".format(exemple.label))
    
    # Ask if want insert a example to be labeled
    mode = 'yes'
    while mode == 'yes':
        mode=raw_input('Try an personal example?[yes/no]\n').lower().strip()
        if mode == 'yes':
            row = []
            for i in id3.attributs.list_attributs:
                row.append(raw_input('The '+i+' is:').lower().strip())
            exemple = Exemple(id3.attributs.list_attributs,row)
            id3.categorize(exemple)
            print("\nlabeled as : '{}'\n".format(exemple.label))
    
    # Create the C45 tree, print 
    # and categorize a exemple
    print '\nC45'
    print('-' * 30)
    c45 = C45(config.file_training_url)
    c45.constructor()
    c45.print_tree()
    exemple = Exemple(["outlook", "temperature", "humidity", "wind"],
                      ["rain",    "mild",        "normal",   "strong"])
    c45.categorize(exemple)
    print("\nlabeled as : '{}'\n".format(exemple.label))
    
    # Ask if want insert a example to be labeled
    mode = 'yes'
    while mode == 'yes':
        mode=raw_input('Try an personal example?[yes/no]\n').lower().strip()
        if mode == 'yes':
            row = []
            for i in c45.attributs.list_attributs:
                row.append(raw_input('The '+i+' is:').lower().strip())
            exemple = Exemple(id3.attributs.list_attributs,row)
            id3.categorize(exemple)
            print("\nlabeled as : '{}'\n".format(exemple.label))    
    print('-' * 30)
    
    # Pruning the C45
    print("C45 - Pruning")
    c45 = C45(config.file_training_url,config.file_depurated_url)
    c45.constructor()
    c45.pruning()
    c45.print_tree()
    exemple = Exemple(["outlook", "temperature", "humidity", "wind"],
                      ["Rain",    "Mild",        "Normal",   "Strong"])
    c45.categorize(exemple)
    print("\nlabeled as : '{}'\n".format(exemple.label))
    # Ask if want insert a example to be labeled
    mode = 'yes'
    while mode == 'yes':
        mode=raw_input('Try an personal example?[yes/no]\n').lower().strip()
        if mode == 'yes':
            row = []
            for i in c45.attributs.list_attributs:
                row.append(raw_input('The '+i+' is:').lower().strip())
            exemple = Exemple(id3.attributs.list_attributs,row)
            id3.categorize(exemple)
            print("\nlabeled as : '{}'\n".format(exemple.label))  
    
    print('-' * 30)

