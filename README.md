# Decision Tree
    
Algorithms ID3 and C4.5 were implemented and the codes run with Python >= 2.7

> the attributes and values are not sensitive
> pruning method only work on C45

##### To run

`$ python Main.py`
    
##### To config

You always can change the configuration on the Configuration.py


Attribut          | default                   | Decription
----------------- | ------------------------- | ----------
file_training_url | 'data/beach.csv'          | File to train
file_depurated_url| 'data/beach_depurated.csv'| File with depurate rows to pruning
splitter          | ','                       | Split file when find this caracter
unknown_values    | ['','-','?']              | values that describe a empty value
min_error         | 1.0                       | min erro to be use at pruning
print_tabs_num    | 0                         | used to format the print method tree
num_split_columns | 1                         | number of columns removed (left side) of the file