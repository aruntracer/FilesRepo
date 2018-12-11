def func():
    print("func() in __name__ex.py")
    print(__name__)
func()
# __name__ builtin variable contains __main__ value if it is called from the same file
# __name__ builtin variable contains __name__ex value if it is called from different file
