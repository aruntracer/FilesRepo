import os
from Dbloadapp import properties
from Dbloadapp import my_functions

path = properties.airport_logs_dir
dirs = os.listdir(path+'/')
for file in dirs:
    if file.endswith('.txt'):
        content = open(path+'/'+file,'r')
        print(file)
        line_count = 1
        for line in content:            
            print(my_functions.get_phone_num(line))
