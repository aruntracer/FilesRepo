# function
def myfnc(a,defa):
    print("my py fn a is {}".format(defa))
    print('secnod value {}'.format(defa))

myfnc('k',2)

def returnhello():
    return('hello')

print(returnhello())

def addition(a,b):
    if(type(a)==type(b)==type(1)):
        return(a+b)
    else:
        return('Sorry!, I need integers only!')

print(addition('1',3))

#filter --gets only the list which passes our condition in def
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))

#lambda expression here we no need to declare function
mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))

# split()
tweet = "go sports! #sports"
print(tweet.split('#')) #op ['go sports! ', 'sports']
print(tweet.split('#')[1]) #op ['sports']

#in
print('x' in [1,2,3]) #op False
print('x' in [1,'x',3]) #op True
