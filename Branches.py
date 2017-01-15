#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# The leaf with the label value
#
class Leaf:
    
    label = None
    
    def __init__(self, label):
        
        if not isinstance(label, str):
            raise TypeError("label needs be str not {}".format(type(label)))
        
        if label == "":
            print("INFO: Label needs be a non empty label")
            
        self.label = label

#
# The node contains 
#   A dic whit chidren
#   A atrribute
#
class Node:
    
    children        = None
    attribut_test   = None
    
    def __init__(self, attribut):
        
        self.children = dict()
        
        if not isinstance(attribut, str):
            raise TypeError("Attribut needs be str not {}".format(type(attribut)))
        
        self.attribut_test = attribut

