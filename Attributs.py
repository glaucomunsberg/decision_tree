#!/usr/bin/python
# -*- coding: utf-8 -*-

from Configuration import Configuration
from Exemple import *
from math import log
from operator import itemgetter

class Attributs:
    
    _file_url       = None
    _config         = None
    list_attributs  = None
    list_exemples   = None

    def __init__(self, file_url=""):
        
        self._file_url  = file_url
        self._config    = Configuration()
        
        # check if the file is possible to open
        if not isinstance(file_url, str):
            raise TypeError("file_url can't be open")
            
        if file_url != "":
            with open(file_url, 'r') as fichier:
                self.list_attributs = fichier.readline().lower().strip().split(self._config.splitter)
                #print 'attributs:'
                #print(self.list_attributs)
                #print 'attributs split:'
                self.list_attributs = self.list_attributs[self._config.num_split_columns:(len(self.list_attributs)-1)]
                #print(self.list_attributs)
                self.list_exemples  = self.list_of_examples(fichier.read().lower().split('\n'),self.list_attributs)
                #print 'examples:'
                #for i in self.list_exemples :
                #    print i.print_example()

        else:
            self.list_attributs = list()
            self.list_exemples = list()
            
    #
    # Return a list of examples with this
    #   label
    #
    def labels_possible(self):
        list_to_return = list()
        
        for exemple in self.list_exemples:
            if not exemple.label in list_to_return:
                list_to_return.append(exemple.label)
                
        return list_to_return

    #
    # Entropy
    #   return_val = 0
    #   S = list of exemples
    #   for each label in set
    #       sub_set with the elements with labels
    #           return_val += |c| * log_2(|c|)
    #   log_2(|S|) - return_val/|S|
    #       
    #
    def entropy(self):
        return_val = 0
        for label in self.labels_possible():
            sub_set = self.labeled_as(label)
            log_sub_set = len(sub_set)
            return_val += log_sub_set * log(log_sub_set, 2)
        return log(len(self), 2) - return_val/len(self)

    # 
    # The biggest attribut
    #   Return the name of label of attr needs be tested
    #
    def biggest_attr(self, ID3=True):
        
        max, return_attr = float("-inf"), ""
        
        for attribut in self.list_attributs:
            if not ID3:
                gain = self.ratio_gain(attribut)
            else:
                gain = self.gain_entropy(attribut)
            
            if gain >= max:
                max, return_attr = gain, attribut
        
        return return_attr

    #
    # List values of attribut
    #
    def list_values_of_attr(self, nom_attribut):
        
        list_return = list()
        for exemple in self.list_exemples:
            # is_in = False
            # for element in list_return:
            #   if element == exemple:
            #       is_in = True
            # if not is_in:
            #   list_return.append(exemple.dict_attributs[nom_attribut])
            
            if not exemple.dict_attributs[nom_attribut] in list_return:
                list_return.append(exemple.dict_attributs[nom_attribut])
                
        return list_return
    
    #
    # Return entropy of nom attribut
    #   get the attributs labeled as 
    #   value_entropy = value sur v de |Sv| * Entropie(Sv)
    #   Gain(S, A) = Entropie(S) - 1/|S| * value_entropy
    #
    def gain_entropy(self, nom_attribut):
        
        value_entropy = 0
        for value in self.list_values_of_attr(nom_attribut):
            
            sub_set_attr = self.attribut_as(nom_attribut, value)
            value_entropy += len(sub_set_attr) * sub_set_attr.entropy()
        
        return self.entropy() - value_entropy/len(self)
    #
    #
    #
    def ratio_gain(self, nom_attribut):
        
        split = self.entropy_set(nom_attribut)
        gain = self.gain_entropy(nom_attribut)
        return gain/split if split != 0 else float("inf")
    #
    # 
    # Most common value of attr
    #
    def most_common_value_of(self, nom_attribut):
        
        dict_frequences = dict()
        
        for exemple in self.list_exemples:    
            if exemple.dict_attributs[nom_attribut] not in dict_frequences:
                dict_frequences[exemple.dict_attributs[nom_attribut]] = 0
            dict_frequences[exemple.dict_attributs[nom_attribut]] += 1
        
        return max(dict_frequences, key=dict_frequences.get)
    
    #
    # Set of examples of this attribut
    #
    def attribut_as(self, nom_attribut, value):
        
        attr_to_return = Attributs()
        attr_to_return.list_attributs = self.list_attributs[:]
        attr_to_return.list_attributs.remove(nom_attribut)
        
        for exemple in self.list_exemples:    
            if exemple.dict_attributs[nom_attribut] == value:
                attr_to_return.list_exemples.append(exemple)
        
        return attr_to_return
    
    # 
    #   Return a set of examples that havel this label
    #
    def labeled_as(self, label):
        attr_to_return = Attributs()
        attr_to_return.list_attributs = self.list_attributs[:]
        
        for exemple in self.list_exemples:
            if exemple.label == label:
                attr_to_return.list_exemples.append(exemple)
        return attr_to_return
    
    #
    # entropy of set
    #
    def entropy_set(self, nom_attribut):
        
        value = 0
        for valeur in self.list_values_of_attr(nom_attribut):
            sub_set = self.attribut_as(nom_attribut, valeur)
            value += len(sub_set) * log(len(sub_set), 2)
        return log(len(self), 2) - value/len(self)
    
    #
    # Check if the attr is discretizable
    #
    def is_discretizable(self, nom_attribut):
        for exemple in self.list_exemples:
            try:
                float(exemple.dict_attributs[nom_attribut])
            except ValueError:
                return False
        return True

    #
    # Return tuples of attributs
    #   ['attr','value']
    #
    def attr_tuples(self):
        list_tuples = list()
        for attribut in self.list_attributs:
            #s'il est discrétisable
            if self.is_discretizable(attribut):
                #on sauvegarde les valeurs de chaque exemple
                value_attr = [exemple.dict_attributs[attribut] for exemple in self.list_exemples]
                list_tuples.append((attribut, value_attr))
        return list_tuples

    #
    # discretizable of attr 
    #
    def c45_discretizable(self, nom_attribut):
        
        negative_value_infinity = float("-inf")
        positive_value_infinity = float("+inf")
        list_intervals          = list()
        indice_borne_inf        = 0
        
        #values_sorted is inicialize with values of attribut in example. After sort.
        values_sorted = [(i, self.list_exemples[i].dict_attributs[nom_attribut]) for i in range(len(self))]
        values_sorted.sort(key=itemgetter(1))
        
        # calc based each value in sort list
        for i in range(1, len(values_sorted)):
            if self.list_exemples[values_sorted[i][0]].label !=  self.list_exemples[values_sorted[indice_borne_inf][0]].label:
                borne_inf = negative_value_infinity
                if len(list_intervals) == 0:
                    #borne_inf = math.inf
                    borne_inf = negative_value_infinity
                else:
                    borne_inf = (float(values_sorted[indice_borne_inf][1]) + float(values_sorted[indice_borne_inf-1][1]))/2
                borne_sup = (float(values_sorted[i][1]) + float(values_sorted[i-1][1])) / 2
                list_intervals.append((borne_inf, borne_sup))
                indice_borne_inf = i
                
        # last interval is positive
        try:
            list_intervals.append((list_intervals[-1][1], positive_value_infinity))
        except Exception, e:
            print e.message,list_intervals,nom_attribut
            
        for exemple in self.list_exemples:
            for intervalle in list_intervals:
                if float(exemple.dict_attributs[nom_attribut]) < intervalle[1]:
                    exemple.dict_attributs[nom_attribut] = intervalle
                    break
    
    #
    # Set empty ou unkown values with 
    #   the commom value of this attribut
    #
    def set_attr_without_value(self):
        
        for example in range(len(self.list_exemples)):
            # if attribut is in dict attribut list
            for nom_attribut in self.list_exemples[example].dict_attributs:
                # and the value is for example '' or '?' or 'unknown' 
                if self.list_exemples[example].dict_attributs[nom_attribut] in self._config.unknown_values:
                    #on isole les éléments ayant la même étiquette
                    sous_ensemble = self.labeled_as(self.list_exemples[example].label)
                    #et on récupère la valeur de ce même attribut la plus
                    #fréquente pour l'assigner à la place du '?'
                    self.list_exemples[example].dict_attributs[nom_attribut] = sous_ensemble.most_common_value_of(nom_attribut)
    
    def __len__(self):
        return len(self.list_exemples)

    #
    # Return an list of examples based at list whit values 
    #   and another with labels of attr
    #
    def list_of_examples(self,exemples, noms_attributs):
        
        list_to_return = list()
        
        for row in exemples:
            attributs = row.lower().strip().split(self._config.splitter)
            if self._config.num_split_columns > 0:
                attributs = attributs[self._config.num_split_columns:len(attributs)]
            #print 'attr->', attributs
            label = attributs[-1] if len(attributs) != len(noms_attributs) else ""
            list_to_return.append(Exemple(noms_attributs,attributs[:len(noms_attributs)],label))
            
        return list_to_return
