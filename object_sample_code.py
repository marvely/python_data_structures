class PartyAnimal:
  x = 0
  name = ""
  def __init__(self, nam):
    self.name = nam
    print "I am constructed"
  
  
  def party(self):  #<--- first parameter, and at least one
    self.x = self.x + 1
    print self.name, "party count", self.x
    
    
  #def __del__(self): #<---- only happens at the end of the program...
   # print "I am destructed", self.x
    
#an = PartyAnimal()

#an.party() # <-- make an object, and can call the party() on it
#an.party()
#an.party()
'''
PartyAnimal.party(an) #<----- self becomes an alies of an.
'''
# what we really doing is making new kinds of things~ can use dir and type() to find out
#print "Type:", type (an)
#print "Dir:", dir(an) # print all the methods

'''
the methods with double underscores are for methods when certain things happen, the certain code will get run
'''
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("JIm")
j.party()

s.party() #<-- the 2nd time it runs, should return 2
'''
j and s are Independent instances 
'''
# create a new class using the existing code above:
class FootballFan(PartyAnimal):
  points = 0
  def touchdown(self):
    self.points = self.points + 7
    self.party()  #<------- inherited from the party animal class and puts here
    print self.name, "points", self.points #<---------- new thing for FootballFan class!
k = FootballFan("Karl")
#k.party()
k.touchdown()