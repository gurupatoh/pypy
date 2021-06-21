class Base:
     def printMe(self): 
         print("Calling method printMe() in class Base.")
class Left(Base):
 def printMe(self):
           super().printMe() 
           print("Calling method printMe() in class Left.") 
class Right(Base):
     def printMe(self):
                super().printMe() 
                print("Calling method printMe() in class Right.") 
class Sub(Right,Left):
     def printMe(self):
                super().printMe() 
                print("Calling method printMe() in class Sub.") 
s = Sub()
s.printMe()