import re
from string import digits



all_symbol = [':',';','~','!','@','#','$','%','^','&','*','(',')','-','','+','`','[',']','{','}','<','>',',','.','<','>','/','?','.']
all_days = ['mon','tue','wed','thu','fri','sat','sun']
all_months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
all_time_zones= ['ist','cst','est','pst','ct','et','pt','utc']

#check whether the give str is number or not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

#get phone number from a line
def get_phone_num(line):
    phone = get_ten_digits(line)
    for i in range(len(phone)):                
        if phone[i] in line:                 
            tn_limit = line.find(phone[i])+12
            #check for space of char next to tn
            if is_number(line[tn_limit-2:tn_limit-1]) is False:                            
                return phone[i]
#get 10 digit number from a line
def get_ten_digits(line):
    try:
        return re.findall("(\d{3}\d{3}\d{4})",line)
    except:
        pass

#get the index of the nth substr in string 
def find_nth_character(str1, substr, n):    
    k = 0
    for index, c in enumerate(str1):
        #print index, c, n  # test
        if c == substr:
            k += 1
            if k == n:
                return index


#remove numbers from string
def remove_numbers(str1):
    remove_digits = str.maketrans('', '', digits)     
    return   str1.translate(remove_digits)

#get splitter
def get_splitter(str1):
        
    for i in range(len(all_symbol)):        
        if len(str1)-len(str.replace(str1, all_symbol[i], '')) == 6:
            return all_symbol[i]

#get formatted date
def get_formatted_date(str1):
    #find day
    for i in range(len(all_days)):    
        if str1.lower().find(all_days[i]) > -1:
            #print('found day '+all_days[i])
            day =  all_days[i]
    
    #find month
    for i in range(len(all_months)):    
        if str1.lower().find(all_months[i]) > -1:
            #print('found month '+all_months[i])
            month = all_months[i]
    
    #find time zone
    for i in range(len(all_time_zones)): 
        if str1.lower().find(all_time_zones[i]) > -1:
            #print('found time zone '+all_time_zones[i])
            time_zone = all_time_zones[i]
    
    #find year
    for i in range(1800,3000): 
        if str1.lower().find(str(i)) > -1:
            #print('found year '+str(i))
            year = i
    
    temp = (str1.lower().replace(day, '').replace(month,'').replace(time_zone,'').replace(str(year),'')).strip()
    #find date
    for i in range(len(all_symbol)): 
        if len(temp)-len(str.replace(temp, all_symbol[i], '')) == 2:
            #print('hour --> '+temp[find_nth_character(temp,all_symbol[i],1)-2:find_nth_character(temp,all_symbol[i],2)-3])
            hour = temp[find_nth_character(temp,all_symbol[i],1)-2:find_nth_character(temp,all_symbol[i],2)-3]
            #print('mins --> '+temp[find_nth_character(temp,all_symbol[i],2)-2:find_nth_character(temp,all_symbol[i],2)])
            mins = temp[find_nth_character(temp,all_symbol[i],2)-2:find_nth_character(temp,all_symbol[i],2)]
            #print('secs --> '+temp[find_nth_character(temp,all_symbol[i],2)+1:find_nth_character(temp,all_symbol[i],-2)])
            secs = temp[find_nth_character(temp,all_symbol[i],2)+1:find_nth_character(temp,all_symbol[i],-2)]
            if int(hour) > 12:
                timeformat = '24HR'
            else:
                timeformat = '12HR'
            date = (temp.lower().replace(all_symbol[i],'').replace(hour,'').replace(mins,'').replace(secs,'')).strip()
            formatted_time = str(hour)+':'+str(mins)+':'+str(secs).strip()+' '+timeformat+' '+day.capitalize()+' '+str(date)+'/'+str(month).capitalize()+'/'+str(year)
            
    return formatted_time
            