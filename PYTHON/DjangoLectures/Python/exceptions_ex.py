try:
    f = open('temp.py','w')
    f.write("wirte one")
except IOError:
    print("Error could not read data")
except:
    print("other error")
else:
    print("success no error")
    f.close()

try:
    f = open('temp.py','r')
    f.write("wirte one")
except IOError:
    print("Error could not read data")
finally:
    print("I will work always")
