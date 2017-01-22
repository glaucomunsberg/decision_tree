#!/usr/bin/python
# -*- coding: utf-8 -*-
from Configuration import Configuration

from Attributs import Attributs
from Exemple import *
from Branches import Node, Leaf

# This tree decision run from 
#   examples gived
class ID3:
    
    _config     = None
    _file_name  = None
    attributs   = None
    tree        = None

    def __init__(self, file_name):
        
        self._config    = Configuration()
        self._file_name = file_name
        
        self.attributs = Attributs(self._file_name)
        self.tree = None

    #
    # Method constructor tree
    #
    def constructor(self):
        self.tree = self.__constructor(self.attributs)
    
    #
    # Tree's constructor (recursive method)
    #
    def __constructor(self, attributs):
        
        if not isinstance(attributs, Attributs):
            raise TypeError("attributs needs be Atrributs type not {}".format(type(attributs)))
        
        if len(attributs) == 0:
            raise ValueError("Number of examples needs be more than 0") # If list empty
        
        # check if entropy of all examples is from the same label
        # return the label if yes
        if attributs.entropy() == 0: 
            return Leaf(attributs.list_exemples[0].label)
        # Test all labels
        if len(attributs.list_attributs) == 0:
            max, label_final = 0, ""
        
            # Each labels possible and finds the most common
            # and return this label
            for label in attributs.labels_possible(): 
                sub_attributs = attributs.labeled_as(label)
                if len(sub_attributs) > max:
                    max, label_final = len(sub_attributs), label
            return Leaf(label_final)

        # finds the biggest attr, create the node with it.
        # for all values with this attr create new node
        # return the node
        biggest_attr = attributs.biggest_attr()
        node = Node(biggest_attr)
        for value in attributs.list_values_of_attr(biggest_attr):
            sub_attributs = attributs.attribut_as(biggest_attr, value)
            node.children[value] = self.__constructor(sub_attributs)
        
        return node
    #
    # categorize
    #
    # categorize (label) the example 
    #   from tree decision
    #
    def categorize(self, exemple):
        
        current_node = self.tree
        # while out of leaf search in nodes
        # update label to the next node explored
        while not isinstance(current_node, Leaf):
            value = exemple.dict_attributs[current_node.attribut_test].lower()
            try:
                current_node = current_node.children[value]
            except:
                print 'Can\'t get value ',value,' from column ',current_node.attribut_test, ' in ',exemple.dict_attributs
                exit()
            
        exemple.label = current_node.label

    #
    # print tree
    #
    def print_tree(self):
        self.__print_tree(self.tree)

    #
    # Print Structure
    #   ->  is the label of the attr
    #   =   is the value of the leaf
    #   |   each label child of the leaf
    #
    def __print_tree(self, node, print_tabs_num=0):
        
        # check if is Node, Leaf
        if isinstance(node, Node):
            print('\t|' * print_tabs_num + node.attribut_test)
            for child in node.children:
                print('\t' * print_tabs_num + '-> ' + str(child))
                self.__print_tree(node.children[child], print_tabs_num+1) #updating the indentation margin
        elif isinstance(node, Leaf):
            print('\t' * print_tabs_num + '= ' + node.label)
        else:
            raise TypeError("Print error, the element needs be Node or Leaf non a {}".format(type(node)))

    

