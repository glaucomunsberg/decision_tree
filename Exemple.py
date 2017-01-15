#!/usr/bin/python
# -*- coding: utf-8 -*-

# examples is assembled with
#   the dict of attributs and a label
class Exemple:
    
    label           = None # if label none Node was no marked 
    dict_attributs  = None

    def __init__(self, noms_attrs, values_attribs, label=""):
        
        # check params type
        if not isinstance(noms_attrs, list) or not isinstance(values_attribs, list):
            raise TypeError("label and attributs needs be a list not {0} and {1}".format(type(noms_attrs),type(values_attribs)))
        if not isinstance(label, str):
            raise TypeError("label needs be str not {}".format(type(label)))
            
        # check if the both are not the same size
        if len(values_attribs) != len(noms_attrs):
            raise ValueError("noms_attrs and values_attribs needs take the same size")
        
        # labeled and dict create based on norms and values received
        self.label          = label
        self.dict_attributs = dict()
        for i in range(len(noms_attrs)):
            self.dict_attributs[noms_attrs[i]] = values_attribs[i]
            
    def print_example(self):
        print 'label ', self.label
        print 'attrs ', self.dict_attributs

