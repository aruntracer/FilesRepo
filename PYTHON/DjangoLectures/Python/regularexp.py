import re

mypatterns = ['term1','term2']
text = "I paid term1 fees"
email = 'solutions@gmail.com'
spiltter = '@'

#re.search searches a match for the string anywhere in the text
for i in mypatterns:
    print("I'm searching for "+i)
    if re.search(i,text):#(keyword,fulltext) can use this as boolean check
        print("match")
    else:
        print("no match")

match = re.search('term1',text)
print(match)#gives the span i.e start index of match term
print(match.start())#give the start index of match term

#Regular expressions beginning with '^' can be used with search() to restrict the match at the beginning of the string:
'''
>>> re.search("^c", "abcdef")  # No match
>>> re.search("^a", "abcdef")  # Match
'''

#re.match searches a match for the string in the beginning of the text can use this as boolean check
print('match result')
print(re.match('term1',text)) #op None
text = "term1 I paid term1 fees"
print(re.match('term1',text)) #op <re.Match object; span=(0, 5), match='term1'>
#re.split
print(re.split(spiltter,email))#op ['solutions', 'gmail.com']
    #or
print(email.split(spiltter))#op ['solutions', 'gmail.com']
#re.findall
print(re.findall('match','test phrase match in match middle')) #op ['match', 'match']

#re.compile here you can compile the patter in a variable and can use for any number of raw text
text1 = 'test phrase match in match middle'
text2 = 'test phrase2 match in end match match'
search_prog = re.compile('match')
print(search_prog.findall(text1))
print(search_prog.findall(text2))

#re.finditer
text1 = 'test phrase 1235 match in 896 match middle'
alpha_iter = re.finditer(r'\D+',text1)
for i in alpha_iter:
    print(i.start())#returns start pos of string match
    print(i.end())#returns end pos of string match

#re.sub replaces the strings with given replace strings
text1 = 'test phrase 1235 match in 896 match middle'
print(re.sub('match','replace',text1)) #op test phrase 1235 replace in 896 replace middle
print(re.sub(r'\d+','replace',text1)) #op test phrase replace match in replace match middle
