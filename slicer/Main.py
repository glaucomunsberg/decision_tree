import glob, os, sys
sys.path.append('../')

from Configuration import Configuration
from random import randint

if __name__ == "__main__":
    config = Configuration()
    
    os.chdir("data/")
    for file_url in glob.glob("*.csv"):
        print file_url
        
        # Compile the urls
        file_training_url   = file_url.split('.')
        file_training_url   = file_training_url[0]+"_training.csv"
        file_test_url       = file_url.split('.')
        file_test_url       = file_test_url[0]+"_test.csv"
        
        # Open the files
        file            = open(file_url, 'r')
        file_test       = open(file_test_url,'w')
        file_training   = open(file_training_url,'w')
        lines = file.readlines()
        
        # Adding header
        file_training.write(lines[0])
        file_test.write(lines[0])
        del lines[0]
        
        # Cal distribution
        training_size   = int(round(len(lines)*config.slicer_percentage))
        test_size       = len(lines)-training_size
        num_line        = 0
        print 'training size: ',training_size,' test_size: ',test_size
        while len(lines) > 0:
            line_number = randint(0, len(lines)-1)
            if num_line < training_size:
                file_training.write(lines[line_number])
            else:
                file_test.write(lines[line_number])
            del lines[line_number]
            num_line += 1
        file_training.close()
        
    
    