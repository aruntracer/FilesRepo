import re

def multi_re_find(keyword,raw_text):
    for pat in keyword:
        print("Search for pattern {}".format(pat))
        print(re.findall(pat,raw_text))
        print('\n')

text = "sdsd..sddds...sddsdd...dsds...dssssss.sddddd"
meta_patterns = ['sd*']#* indicates s is followed by zero or more occurences of d
meta_patterns1 = ['sd+']#* indicates s is followed by one or more occurences of d
meta_patterns2 = ['sd?']#* indicates s is followed by zero or one occurences of d
meta_patterns3 = ['sd{3}']#* indicates s is followed by three occurences of d
meta_patterns4 = ['sd{2,3}']#* indicates s is followed by two or three occurences of d
meta_patterns5 = ['s[sd]+']#* indicates s is followed by one or more s or d

multi_re_find(meta_patterns,text)#['sd', 'sd', 'sddd', 's', 'sdd', 'sdd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd']
multi_re_find(meta_patterns1,text)#['sd', 'sd', 'sddd', 'sdd', 'sdd', 'sd', 'sddddd']
multi_re_find(meta_patterns2,text)#['sd', 'sd', 'sd', 's', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']
multi_re_find(meta_patterns3,text)#['sddd', 'sddd']
multi_re_find(meta_patterns4,text)#['sddd', 'sdd', 'sdd', 'sddd']
multi_re_find(meta_patterns5,text)#['sdsd', 'sddds', 'sddsdd', 'sds', 'ssssss', 'sddddd']

text_punc = "Hi this is sol, welcome to my page!, Having a good day"
meta_patterns6 = ['[^,!?]+']# indicates to split based on the given symbols, text before the symbol will be stripped out
meta_patterns7 = ['[a-z]+']# indicates to list all the lower case chars

multi_re_find(meta_patterns6,text_punc)#['Hi this is sol', ' welcome to my page', ' Having a good day']
multi_re_find(meta_patterns7,text_punc)#['i', 'this', 'is', 'sol', 'welcome', 'to', 'my', 'page', 'aving', 'a', 'good', 'day']


''' the 'r' means the the following is a "raw string", ie. backslash characters are treated literally instead of signifying special treatment of the following character.
#
# http://docs.python.org/reference/lexical_analysis.html#literals
#
# so '\n' is a single newline
# and r'\n' is two characters - a backslash and the letter 'n'
# another way to write it would be '\\n' because the first backslash escapes the second'''

text_num = "Hi this is 2324332 number 234233 ? good"
meta_patterns7 = [r'\d+']# indicates to list all the digits op - ['2324332', '234233']
meta_patterns7 = [r'\D+']# indicates to list all the non digits op - ['Hi this is ', ' number ', ' ? good']
meta_patterns7 = [r'\s+']# indicates to list all the whitespaces op - [' ', ' ', ' ', ' ', ' ', ' ', ' ']
meta_patterns7 = [r'\S+']# indicates to list all the non whitespaces op - ['Hi', 'this', 'is', '2324332', 'number', '234233', '?', 'good']
meta_patterns7 = [r'\w+']# indicates to list all the alpha numeric op - ['Hi', 'this', 'is', '2324332', 'number', '234233', 'good']
meta_patterns7 = [r'\W+']# indicates to list all the non alpha numeric op - [' ', ' ', ' ', ' ', ' ', ' ? ']
multi_re_find(meta_patterns7,text_num)
