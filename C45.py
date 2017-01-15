#!/usr/bin/python
# -*- coding: utf-8 -*-

from Configuration import Configuration

from Attributs import Attributs
from Exemple import *
from ID3 import ID3
from Branches import Node, Leaf

#
# The C45 tree inherits a ID3 and build 
#
class C45(ID3):
    
    file_url        = None
    pruning_method  = None
    tree            = None
    attributs       = None
    _config         = None

    def __init__(self, file_url, pruning_method=""):
        self._config        = Configuration()
        self.file_url       = file_url
        self.pruning_method = pruning_method
        
        self.tree       = None
        self.attributs  = Attributs(self.file_url)
                

    def constructor(self):
        self.attributs.set_attr_without_value()
        self.tree = self.__constructor(self.attributs)

    def __constructor(self, attributs):
        
        if len(attributs) == 0:
            raise ValueError("The list can't be empty")
        
        if not isinstance(attributs, Attributs):
            raise TypeError("The attribut needs by Attributs type")
        
        # 1 - Return the label if entropy == 0
        if attributs.entropy() == 0:
            return Leaf(attributs.list_exemples[0].label)
        
        # 2 - if not, test the best attribut to return
        if len(attributs.list_attributs) == 0:
            max, label_final = 0, ""
            for label in attributs.labels_possible():
                labeled_as = attributs.labeled_as(label)
                if len(labeled_as) > max:
                    max, label_final = len(labeled_as), label
            return Leaf(label_final)

        # 3a - save in case of attr not discretized
        # discretize all values
        backup_values = attributs.attr_tuples()
        for attribut, values in backup_values:
            attributs.c45_discretizable(attribut)
            
        # 3b - restore the best attr and the labels
        # for all backup values, 
        # if not the selectable attr
        #   give the old continuous values
        biggest_attr = attributs.biggest_attr(False)
        for attribut, values in backup_values:
            if attribut != biggest_attr:
                for i in range(len(values)):
                    attributs.list_exemples[i].dict_attributs[attribut] = values[i]
                    
        # 3c - return the node not a leaf
        # for each value that can be test
        #   create a sub-attrs and create the new node
        #   #__constructor needs be used remove the __constructor2
        # return the node created
        node = Node(biggest_attr)
        for value in attributs.list_values_of_attr(biggest_attr):
            attribut_as = attributs.attribut_as(biggest_attr, value)
            node.children[value] = self.__constructor(attribut_as)
        return node

    def categorize(self, exemple):
        
        current_node = self.tree
        
        # while out of leaf search in nodes
        #   get value from the nood tested
        #   if the value is number like float
        #       than is a discretable value
        #   else 
        #       the value is constant need be converted to interval
        #   get the current_node to child value
        # the example will be rotulate with the node label from end the exploration =D
        while isinstance(current_node, Node):
            value = exemple.dict_attributs[current_node.attribut_test].lower()
            try:
                value = float(value)
            except:
                pass
            else:
                for interval in current_node.children:
                    if value < interval[1] and value >= interval[0]:
                        value = interval
                        break
            finally:
                current_node = current_node.children[value]
        exemple.label = current_node.label
        
    #
    # Pruning
    #   change the tree
    #
    def pruning(self):
        print 'pruning...'
        if self.pruning_method != "":
            self.tree = self.__pruning_node(self.tree,Attributs(self.pruning_method))

    #
    # pruning_node is a recursive method that receive the
    #   node and return the pruning from this node
    #
    def __pruning_node(self, node, set_pruning):
        
        # if is the node a Leaf
        #   return the node
        if isinstance(node, Leaf):
            return node
        
        min_error   = 1.0
        label_held  = ""
        initial_proportion  = self.error_rate(set_pruning)
        backup_tree         = self.tree
        
        # else 
        #   for all possibles labels
        #       create the leaf label
        #       calcule the error rate
        #       if error is less than the min_error
        #           update the min_error and label for the labels
        #   
        for label in set_pruning.labels_possible():
            self.tree = Leaf(label)
            #on calcule le taux d'erreur si on remplace le nœud par
            #l'étiquette en question
            current_error_tax = self.error_rate(set_pruning)
            #on backup_tree  le meilleur taux
            if current_error_tax < min_error:
                min_error   = current_error_tax
                label_held  = label
                
        # if the tax is not good 
        #   return the leaf
        # else 
        #   restaure the tree
        # Each child from children
        #   find the attribus > 0
        #       pruning them
        if min_error <= initial_proportion:
            return Leaf(label_held)
        else:
            self.tree = backup_tree 
        
        backup_tree = self.tree
        self.tree  = backup_tree 
        
        for child in node.children:
            attribut_as = set_pruning.attribut_as(node.attribut_test,child)
            if len(attribut_as) != 0:
                node.children[child] = self.__pruning_node(node.children[child],attribut_as)
        return node
    
    #
    # Error Rate
    #   return the proportion of examples 
    #   labeled correctly based on file's rodulation
    #
    def error_rate(self, attributs):
        
        number_labels_incorrect = 0
        # for each example of examples
        # if label != label from example
        #   sum one the incorrect label
        #   if wrong then restore the label
        # return the number of incorrect label divided by attributs size
        
        for exemple in attributs.list_exemples:
            label = exemple.label
            self.categorize(exemple)
            if label != exemple.label:
                number_labels_incorrect += 1
                exemple.label = label
        return number_labels_incorrect/len(attributs)