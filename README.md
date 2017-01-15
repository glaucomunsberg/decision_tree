# Decision Tree
    
Algorithms ID3 and C4.5 were implemented and the codes run with Python >= 2.7

#### Run

`$ python Main.py [-id3|-c45|-c45p] [-t|-d|-i|-o FILE_PATH]`

Attribute | Description
--------- | -----------
`-id3`    | Execute the ID3 algorithm
`-c45`    | Execute the C45 algorithm
`-c45p`   | Execute the C45 algorithm with pruning
`-t FILE` | Change the default file to train
`-d FILE` | Change the default file used on -c45p
`-i FILE` | File input with examples that you want test
`-o FILE` | File outut with results from examples tested by the algoritm

#### Config

You always can change the configuration on the Configuration.py


Attribute         | Default value             | Description
----------------- | ------------------------- | -------------
file_training_url | 'data/beach.csv'          | File to train
file_depurated_url| 'data/beach_depurated.csv'| File with depurate rows to pruning
file_examples_url | 'data/examples.csv'       | File with examples
file_output_url   | 'data/output.csv'         | File output
splitter          | ','                       | Split file when find this caracter
unknown_values    | ['','-','?']              | values that describe a empty value
min_error         | 1.0                       | min erro to be use at pruning
print_tabs_num    | 0                         | used to format the print method tree
num_split_columns | 1                         | number of columns removed (left side) of the file

#### Notes

> the attributes and values are not sensitive

> pruning method only work on C45
