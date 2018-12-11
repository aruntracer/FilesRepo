from random import randint

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
randval = list(str(randint(100,999)))
flushme = "run"
print(randval)
print("Code has been generated, please guess a 3 digit number")

while flushme is not None:
    inputval = list(input("What is your guess?"))
    if randval[0] == inputval[0] and randval[1] == inputval[1] and randval[2] == inputval[2]:
        print("match")
        flushme = None
    elif randval[0] in inputval or randval[1] in inputval or randval[2] in inputval:
        print("close")
    else:
        print("nope")
