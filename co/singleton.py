class OneOnly:
   _singleton = None
   def _new_(cls, *args, **kwargs):
      if not cls._singleton:
          cls.singleton = super(OneOnly, cls).new_(cls, *args, **kwargs)
      return cls._singleton
class GameManager: 
     def __eq__(self,object):
         print(id(self))
         print(id(object))

         if id(self)==id(object): 
              print("We are the same object because we have the same object ID!")
              return True 
         else: 
            print("We are not the same object!") 
            return False 
g1 = GameManager() 
g1.__eq__
g2 = GameManager() 

g1==g2
