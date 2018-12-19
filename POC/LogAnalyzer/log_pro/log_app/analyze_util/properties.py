import time,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#log_pro path
airport_logs_dir = os.path.join(BASE_DIR,"static","AirportLogs")
report_dir = os.path.join(BASE_DIR,"static","AirportLogs","Report")
airport_file_name = os.path.join(report_dir,'Airport_Log_'+str.replace(str.replace(time.ctime(),' ','_'),':','_')+'.csv')
airport_col_name = [['FILE_NAME','DATE','SIM_NUMBER','TN','NAME','PLAN_NAME','SITE_ID','SITE_NAME']]
