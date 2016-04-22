#inheritance

#Miembro de la escuela
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name:{} Age:{}'.format(self.name, self.age))

#El docente es un miembro de la escuela

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)#heredando el constructor del padre
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)#veras como un docente es un miembro
        print('Salary: {:d}'.format(self.salary))
#El estudiante es un miembro de la escuela

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {:d}'.format(self.marks))


t = Teacher('Mrs. Shrividya',40,30000)
s = Student('Swaroop',25,75)

members=[t,s]
for member in members:
    member.tell()



      

    

