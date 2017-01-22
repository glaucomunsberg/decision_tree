import sys
sys.path.append('../')

from C45 import C45
from ID3 import ID3
from Configuration import Configuration
from Exemple import Exemple

if __name__ == "__main__":
    
    config = Configuration()
    
    c45 = C45('training.csv','training_depurated.csv')
    c45.constructor()
    c45.print_tree()
    with open('examples.csv') as f:
            lines = f.readlines()
            row_num = 0
            for line in lines:
                row = line.lower().strip().split(config.splitter)
                exemple = Exemple(c45.attributs.list_attributs,row)
                c45.categorize(exemple)
                print 'row ',row[0]
                print("\nlabeled as : '{}'\n".format(exemple.label))
                row_num+=1