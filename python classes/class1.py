class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author


b1=Book("Brave new world","Arjit")
b2=Book("Seven Habbit of highly effective teenagers","Anshika") 
#print(b1)
print("The book "+b1.title+" is written by "+b1.author)   
print("The book "+b2.title+" is written by "+b2.author)       
