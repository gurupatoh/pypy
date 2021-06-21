class NewspaperSubscriber:
    def __init__(self,arg) -> None:
        self.arg=arg
        pass
    def addHeadline( headline):
        print(' got message "{}"'.format( headline))


class NewspaperHeadlines:
     def __init__(self): 
         self.headlines = [] 
     def latestHeadline(self): 
         return self.headlines[-1] 
     def addHeadline(self, headline):
         NewspaperSubscriber.addHeadline(headline)
     def subscribe(self,headline):
         pass



h = NewspaperHeadlines() 
s = NewspaperSubscriber(h)
h.subscribe(s)
h.addHeadline("Severe weather warning for tomorrow.")
h.addHeadline("Sever weather warning cancelled.")
