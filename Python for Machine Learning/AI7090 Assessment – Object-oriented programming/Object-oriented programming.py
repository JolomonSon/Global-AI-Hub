'''
# Question 1
class favLanguage:
    def printLine(self, language="Python"):
        print(language)

myObject = favLanguage()
myObject.printLine("Java")

class Sales:
    def __init__(self, id):
        self.id = id
        id = 100
val = Sales(123)
print(val.id)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x + 1
        self.y = y + 1
p1 = Point()
print(p1.x, p1.y)



name=input("Enter your name")
age=input("Enter your age")
if name >= 18:
    print("Hello,",name,"You are not eligible to vote")
else:
    print("Hello,",name,"You are eligible to vote")
'''

