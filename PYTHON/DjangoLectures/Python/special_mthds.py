class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("Book is destroyed")
bojb = Book("My Book","My Author",189)
print(bojb) #initial op without __str__ inclustion <__main__.Book object at 0x000001BE7D1D8240>
print(len(bojb))
del(bojb)
print(len(bojb))#not accessible since book obj is destroyed using del method
