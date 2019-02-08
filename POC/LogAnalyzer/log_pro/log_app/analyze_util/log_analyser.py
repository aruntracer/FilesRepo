import os
from log_analyzer.properties import airport_logs_dir,airport_file_name,airport_col_name
from log_analyzer.my_functions import find_nth_character,remove_numbers,get_splitter,get_formatted_date
import csv
#import cx_Oracle
import mysql.connector
import sys

log_file = open(airport_file_name, 'w',newline='')
writer = csv.writer(log_file)
writer.writerows(airport_col_name)

path = airport_logs_dir
dirs = os.listdir(path+'/')
for file in dirs:
    if file.endswith('.txt'):# and file == 'Airport2G20131218210630.txt':
        content = open(path+'/'+file,'r')
        #print(file)
        for line in content:            
            spillter = get_splitter(line)
            Date = get_formatted_date(line[:find_nth_character(line,spillter,1)])
            Simnumber = '-'+str(line[find_nth_character(line,spillter,1)+1:find_nth_character(line,spillter,2)])+'-'
            Tn = line[find_nth_character(line,spillter,2)+1:find_nth_character(line,spillter,3)]
            Name = remove_numbers(line[find_nth_character(line,spillter,3)+1:find_nth_character(line,spillter,4)]).strip()
            Plan = line[find_nth_character(line,spillter,4)+1:find_nth_character(line,spillter,5)]
            Site_Id = line[find_nth_character(line,spillter,5)+1:find_nth_character(line,spillter,6)]
            Site_Name = line[find_nth_character(line,spillter,6)+1:find_nth_character(line,spillter,7)]
            
            row_data = [[file,Date,Simnumber,Tn,Name,Plan,Site_Id,Site_Name]]
            log_file = open(airport_file_name, 'a',newline='')
            with log_file:
                writer = csv.writer(log_file)
                writer.writerows(row_data)
                
try:
    #con = cx_Oracle.connect('arun1297/arun1297@bdes059.prodapt.com:1521/orcl.prodapt.com')
	#cur = con.cursor()
	con = mysql.connector.connect(host="192.168.26.120",user="root",passwd="root",database="log_analyser" )
	cur = con.cursor()
except:    
    sys.exit('DB connection error: '+str(sys.exc_info()[1]))
with open(airport_file_name) as csv_file:                  
    readcsv = csv.reader(csv_file)
    for row in readcsv:
        try:                
            if row[0] != 'FILE_NAME':                
                #print("insert into data_collector values('"+row[0]+"','"+row[1]+"',"+str.replace(row[2],'-','')+","+str.replace(row[3],"'","''")+",'"+str.replace(row[4],"'","''")+"','"+row[5]+"','"+row[6]+"','"+row[7]+"')")
                insert_row ="insert into data_collector values('"+str.replace(row[0],"'","''")+"','"+str.replace(row[1],"'","''")+"',"+str.replace(row[2],'-','')+","+str.replace(row[3],"'","''")+",'"+str.replace(row[4],"'","''")+"','"+str.replace(row[5],"'","''")+"','"+str.replace(row[6],"'","''")+"','"+str.replace(row[7],"'","''")+"')"
                cur.execute(insert_row)                
        except:            
            print('Skipped -- '+row[0]+", "+str(sys.exc_info()[1]))
            insert_row ="insert into data_collector values('"+row[0]+"','"+str.replace(str(sys.exc_info()[1]),"'","''")+"')"
            cur.execute(insert_row)
            pass
con.commit()
cur.close()
con.close()            
