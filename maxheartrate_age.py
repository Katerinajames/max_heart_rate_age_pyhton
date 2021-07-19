
from datetime import date

class Date():
 daysPerMonth=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
	
 def  __init__(self,month,day,year):
             
             if 0 < month <= 12:
                self.month=month
             else:
                raise ValueError, "Invalid value for month: %d" % month                
                self.day=self.checkDay(day)
             if year >= 0:
                self.year = year
             else:
                 raise ValueError, "Invalid value for year: %y" % year 
             self.day=self.checkDay(day)     
             


 def checkDay(self,testDay):

        if 0 < testDay <= Date.daysPerMonth[self.month]:
           return testDay
        elif self.month == 2 and testDay == 29 and ( self.year % 400 == 0 or self.year % 100 != 0 and self.year % 4 == 0 ):
           return testDay
        else:
         raise ValueError, "Invalid day: %d for month: %d" % ( testDay, self.month )
       






print"----------------------------------------------"

class Heartbeat:
 def  __init__(self,first,last,p):
        self.first=first
        self.last=last 	  
        self.p=p
 def calculate(self):
    today=date.today()
    age=today.year-p.year -((today.month, today.day) <(p.month, p.day)) 
    return age
 def maxheartrate(self):
     rate=220-k.calculate()	     
     return rate	    
    

print"----------------------------------------------"

p=Date(5,21,1970)



k=Heartbeat("Kat","Stephens",p)






print "My age is",k.calculate()
print "My max heart rate is ",k.maxheartrate()


