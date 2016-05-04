#relacion de uno amuchos

class Person:
    def __init__(self,name,job='None',pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))
    def __str__(self):
        return 'Person: %s, %s' % (self.name,self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr) # Delegate all other attrs
    def __str__(self):
        return str(self.person)


class Department:
    def __init__(self ):
        self.members=[]
        
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

bob = Person('Frank Kafka',pay=1000.00)
sue = Person('Karen Cardona',job='Programmer',pay=500.00)

development = Department() # Embed objects in a composite
tom=Person('La web de el programador',pay=700)
development.addMember(bob)
development.addMember(sue)
development.addMember(tom)
development.giveRaises(.10) # Runs embedded objects' giveRaise
development.showAll()

    
        
