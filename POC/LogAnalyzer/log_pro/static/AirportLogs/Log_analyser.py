import os, sys
from pathlib import Path
path = "D:\Projects\Antony_POC\Log_Analyser\sample_logs\Log_Airport_Signal\"
dirs = os.listdir(path)
for file in dirs:
    if file.endswith('.txt'):
        content = open(file,'r').read().replace('\n',' ')
        simnumber = content[29:44]
        phonenumber = content[45:55]
        username = content[56:72]
        #print (type(content))
        print ('simnumber :: ' + simnumber + ' phonenumber :: ' + phonenumber + ' username :: ' + username )
        
    
    
    
    
    
    
	    
    
    
