mysting = 'arunakumar'
# index
# print(mysting[3])
# slicing
# print(mysting[2:])
# print(mysting[:2])#before but not including the 2 index

# x = mysting.split('a')
# op ['', 'run', 'kum', 'r']
# print formatting
# a = 'arun'
# b = 'kumar'
# x = "item one {} item two {}".format(a,b)
# x = "item one {b} item two {b}".format(a = 'arun',b = 'kumar')
# print(x)
# lists
# mylist = [1,2,3]
# mylist = ['arun',1,2,23.44,True,'asad',[1,2,3]]
# print(mylist)# op ['arun', 1, 2, 23.44, True, 'asad', [1, 2, 3]]
# print(mylist[6][1])#op 2
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# first_col = [row[0] for row in matrix]
# print(first_col)
# dictionaries
# my_stuff = {"key1":"arun","key2":"Nive"}
# print(my_stuff['key2'])
#tuples
# t = (1,2,3)
# print(t[2])
# t[0] = 'new' #this will throw error since tuples are immutable but we can do this with lists [] instead of tuples ()
#  sets unorder set of unique elements
# s = set()
# s.add(1)
# s.add('arun')
# s.add(1)
# print(s)#{1, 'arun'}


# list comprehension
x = [1,2,3,4]
# out = []
# for num in x:
#     out.append(num**2)
# print(out)
# or
out = [num**2 for num in x]
print(out)
