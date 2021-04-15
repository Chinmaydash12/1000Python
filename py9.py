'''a=5
def add():
    a=10
    print(a)
    def sub():
        print(a)
        b=30
        print(b)
    print(a)
    sub()
add()
print(a)'''

'''a=5
def add():
    print(a) 
    a=10
    print(a)
add()'''

'''a=5
def add():
   global a
   a=10
   def sub():
       nonlocal a
       a=20
       print(a) # global and nonlocal annot put together
   print(a)
   sub()
   print(a)
print(a)
add()
print(a)'''
#Using continue , by using continue the particular cond will satisfy(skip)
'''for x in range(1,51):
    if x%2==0:
        continue
    print(x)'''
'''for x in range(1,31):
    if x%2==0 or x%3==0: #it satisfying both condition 
        continue
    print(x)'''
#Using break , by using break statement the part after condition will not come
'''for x in range(1,21):
    if x==10:
        break
    print(x)'''
#Using pass ,  y using pass the if block condition will satisfy by else only simply by passin if
'''for x in range(1,31):
    if x%2!=0:   
        pass
    else:
        print(x) '''   #the output no.s will divisible by 2

'''class indi:
     hii connections
print(indi.__doc__)
help(indi)'''
#Class with hardcode
'''class indi:
    def __init__(self):
        self.name='Chinmay'
        self.age=23
        self.weight=64
    def about(self):
        print('My name is ',self.name)
        print('My age is ',self.age)
        print('My weight ',self.weight)
obj=indi()                  #obj is the reference variable for class object indi
#print(obj.about())         # obj will access class method attributes
#obj.about()
print(obj.name)
print(obj.age)
print(obj.weight)'''

#Class with variable passing
'''class hindi:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def work(self):
        print('My name is ',self.name)
        print('My age is ',self.age)
        print('My weight is ',self.weight)
obh=hindi('Chinmay',23,64)      # here ref var obh accessed method attributes
print(obh.name)
print(obh.age)
print(obh.weight)
obh.work()'''

#self is the reference variable to the crrent object within the class

'''class T:
    def __init__(self):
        print('Address of self :',id(self))
a=T()
print('Address of a :',id(a))'''
#we are not going to provide the value of self python is responsible for that
#at the time of objct or reference variable creation constructor will called automatically
#self is used for calling instance variable
'''class A:
    def __init__(self):
        print('constructor')
    def h(self,x):
        print('Value of x: ',x)
t=A()
t.h(10)'''

#self calling
'''class Student:
    def __init__(self):
        print('Hello')
    def D(self,name,rollno,age):
        print('My name is :',name)
        print('My rollno is :',rollno)
        print('My age is: ',age)
t=Student()
t.D('Chinmay',11,23)'''

#Constructor is to initialize and declare instance variable
'''class T:
    def __init__(self):
        print('hello Python')
ty=T()                    #by declaring object constructor automatically called and you will get output
ty.__init__() '''      #constructor can be call explicitly no issue

#Method overloading is not available in Python
#if we are taking two constuctor Python virtual machine will consider the most recent constructor
'''class tym:
    def __init__(self):        #for this program the first will not work
        print('Hii')
    def __init__(self,x):
        print('I am : ',x)
#t=tym()       #it will be not work 
t1=tym(30)
t2=tym(20)'''

#Cricket program
'''class Cric:
    def __init__(self,batsman,bowler,keeper):
        self.batsman=batsman
        self.bowler=bowler
        self.keeper=keeper
    def team(self):
        print('Bats is :',self.batsman)
        print('Bowler is :',self.bowler)
        print('Keeper is :',self.keeper)
playerlist=[]
while True:
    batsman=input('Enter the batsman name: ')
    bowler=input('Enter the bowler name: ')
    keeper=input('Enter the keeper name: ')
    t=Cric(batsman,bowler,keeper)
    playerlist.append(t)
    print('Team created successfully :)')
    option=input('Do you want to create one more team ! [Yes|No] ')
    if option.lower()=='no':
        break
print('Your team details :')
for ty in playerlist:
    ty.team()
    print()'''

#getter setter not used
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hii : ',self.name)
        print('Your marks is :',self.marks)
    def grade(self):
        if self.marks>=60:
            print('First Grade')
        elif self.marks>=50:
            print('Second Grade')
        elif self.marks>=30:
            print('Third Grade')
        else:
            print('Not appeared')
n=int(input('Enter no of students : '))
for i in range(n):
    a=input('Enter your name: ')
    b=int(input('Enter your marks: '))
    m=Student(a,b)
    m.display()
    m.grade()
    print('_'*20)'''

#In Python class name and method name can be same syntactically okay but not recomended
'''class boy:
    def boy(self):
        print('Hello')
a=boy()
a.boy()'''

#variable types(instance varible,static varible,local variable)
'''class student:
    schoolname='DS'    #static variable
    def __init__(self,name,rollno):
        self.name=name       #instance variable
        self.rollno=rollno  #instance variable
    def info(self):
        x=10            # x is local variable
        for i in range(x):     #i is local variable
            print(i)
t=student('Raju',10)
t.info()'''

#Types of Method (Instance method,Class method,Static method)
'''class T:
    @classmethod      #use to access class level variable
    def m(a):     #class level reference variable
        print(id(a))  
print(id(T))
T.m()'''

'''class toy:
    toyname='gulu'
    def __init__(self,name,age):     #constructor
        self.name=name
        self.age=age
    def n(self):              #instance method
        print('Name i: ',self.name)
        print('Age is: ',self.age)
    @classmethod     #class method
    def m(cls):
        print('Toy name: ',cls.toyname)     #here cls refer to class level variable that is static variable
    @staticmethod       #class method
    def o(a,b):     #here a,b are local variable
        sum=a+b
        return sum
t=toy('Hari',10)
t.n()
t.m()
print(t.o(10,12))'''

#Instance Variable

'''class d:
    def __init__(self):
        self.a=10
        self.b=20
t=d()              # a,b will add to object by calling class through reference variable
print(t.__dict__)  '''        #by using __dict__ we will get varible and its value in dictionary format

#instance variable inside instance method

'''class d:
    def __init__(self):
        self.a=10
        self.b=20
    def g(self):      #here instance variable declared inside instance method
        self.c=40
t=d()                #a,b will add to object
t.g()                #cnwill add to object
print(t.__dict__) '''

#declaring instance variable outside of the class through object reference (Only available in Python)

'''class d:
    def __init__(self):
        self.a=10
        self.b=20
    def g(self):      #here instance variable declared inside instance method
        self.c=40
t=d()                #a,b will add to object
t.g()                #c will add to object
t.d=60              # d value is added by object reference
print(t.__dict__) '''

#Number of instance variable varied for object to object only in Python

'''class d:
    def __init__(self):
        self.a=10
        self.b=20
    def g(self):      #here instance variable declared inside instance method
        self.c=40
t=d()                #a,b will add to object
t.g()                #c will add to object
t.d=60              # d value is added by object reference
t1=d()
print(t1.__dict__)     #for t1 and t the instance variable are deifferent
print(t.__dict__)'''

#Multiple Inheritance
'''class Employee:     #first class
    noofday=5
    def __init__(self,ename,esalary,erole):
        self.ename=ename
        self.esalary=esalary
        self.erole=erole
    def about(self):
        return f"The name is {self.ename}. Salary is {self.esalary}.Role is {self.erole}"
    @classmethod
    def changeday(cls,day):
        cls.noofday=day
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printbetter(string):
        print('This is better'+string)
class movie:      #second class
    noofday=2
    def __init__(self,name,filmd):
        self.name=name
        self.filmd=filmd
    def info(self):
        return f"Movie name is {self.name} and release date is {self.filmd}"

class Both(Employee,movie):    #this child class using multiple inheritance
    pass                        #here employee mentioned first thats why we have pass variable to object according to first class method

gudu=Employee('Gudu',25000,'Developer')
butu=Employee('Butu',30000,'Scientist')

ludo=movie('Ludo','Sept')

nov=Both('kulu',40000,'Teacher')
print(nov.about())'''

#Access Instance variable

'''class info:
    def __init__(self):
        self.a=10
        self.b=20
    def val(self):
        print('a= ',self.a)  #accessing inside class
        print('b= ',self.b)
t=info()
t.val()
print(t.a)         #accessing ouside the class through reference variable
print(t.b)'''

# Deleting instance variable

'''class info:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def g(self):
        del self.c      #deleting instance variable inside instance method
t=info()
t.g()
del t.b                 #deleting instance variable outside of class
print(t.__dict__)
t1=info()            #the number of instance variable varies from object to object
del t1.a,t1.b           #deleting multiple instance variable 
print(t1.__dict__) '''    #in the case of t and t1 instance variable are different 

#for every object reference separate copy of instance variable is there
'''class god:
    c=50
    def __init__(self):
        self.a=10
        self.b=20
    def mu(self):
        self.d=40
w=god()
w.a=22
w.b=33
w1=god()
#print('w',w.a,w.b)
#print('w1',w1.a,w1.b)
print(god.__dict__)     ''' #calling static variable using class name

#static variable declaration at different places

'''class D:
    a=12               #static variable outside of constructor and method
    def __init__(self):
        D.b=22          #static variable inside constructor using class name
    def we(self):
        D.c=32         #static variable inside instance method using class name
    @classmethod
    def we1(cls):
        cls.e=42       #inside class method using cls keyword 
        D.f=52         #inside class method using class name
    @staticmethod
    def we2():
        D.g=62         #inside static method using class name
d=D()
d.we()
D.we1()
D.we2()
D.h=72                 #outside of class using class name
print(D.__dict__)'''

#Access static variable at different places

'''class fog:
    a=42
    def __init__(self):
        print(self.a)             #inside constructor using self keyword
        print(fog.a)              #inside constuctor using class name
    def r1(self):
        print(self.a)             #inside instance method using self keyword
        print(fog.a)             #inside instance method using   class name
    @classmethod
    def r2(cls):
        print(cls.a)            #inside class method using cls keyword 
        print(fog.a)          #inside class method using class name
    @staticmethod
    def r3():
        print(fog.a)          #inside static method using class name
r=fog()
r.r1()
fog.r2()
fog.r3()
print('v=',r.a)               #outside class using object reference
print('v2=',fog.a) '''         #outside class using class name

#modify value of static variable

'''class red:
    a=10
    def __init__(self):
        red.a=20           #modification of static variable
    def p(self):
        red.a=30          # modifying value inside instance method using class name
    @classmethod
    def p1(cls):
        cls.a=40          #inside class method using cls variable
        red.a=50          #inside class method using class name
    @staticmethod
    def p2():
        red.a=60         #inside static method using class name
print(red.a)
r=red()                   #by declaring object reference we calling constructor
print(red.a)
r.p()
print(red.a)

red.p1()
print(red.a)
red.p2()
print(red.a)
#print              
red.a=70                #outside class using class name
print(red.a)'''

#Questions
'''class F:
    a=10
    def m(self):
        self.a=888      #with self it is instance variable
t=F()
t.m()
print(F.a)
print(t.a)'''

'''class F:
    a=10
    def m(self):
        F.a=888       #overide with class name so after calling object reference this value will reflect
t=F()
t.m()
print(F.a)
print(t.a)'''

'''class A:
    a=10
    def __init__(self):
        self.b=20
t1=A()
t2=A()
print('t1',t1.a,t1.b)
print('t2',t2.a,t2.b)
t1.a=888             #with object reference we cannot change the value of static variable
t1.b=999              # so a new instance variable a added to the the constructor
print('t1',t1.a,t1.b)
print('t2',t2.a,t2.b)'''

'''class A:
    a=10
    def __init__(self):
        self.b=20
t1=A()
t2=A()
print('t1',t1.a,t1.b)   #before modification
print('t2',t2.a,t2.b)
A.a=888          #it will override the value of static variable a
A.b=999          #but in this case it won't change the instance variable but a new static variable b will declare
print('t1',t1.a,t1.b)   #in Python static variable and inctance variable can be in same name
print('t2',t2.a,t2.b)
print('A',A.a,A.b)'''

'''class A:
    a=10
    def __init__(self):
        self.b=20
t1=A()
t2=A()
A.a=888
t1.b=999
print('t1',t1.a,t1.b)
print('t2',t2.a,t2.b)'''

'''class k:
    a=10
    def __init__(self):
        self.b=20
    def k1(self):
        self.a=888
        self.b=999
t1=k()
t2=k()
t1.k1()
print('t1',t1.a,t1.b)
print('t2',t2.a,t2.b)'''

'''class k:
    a=10
    def __init__(self):
        self.b=20
    def k1(self):
        self.a=888
        self.b=999
t1=k()
t2=k()
t1.k1()
t2.k1()
print('t1',t1.a,t1.b)
print('t2',t2.a,t2.b)'''

'''class k:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def k1(cls):
        cls.a=888
        cls.b=999
t1=k()
t2=k()
print('t2',t2.a,t2.b)
t1.k1()
print('t1',t1.a,t1.b)     #first preference is instance variable s
print('t2',t2.a,t2.b)     #once static variable change one object reference mean it wil affect another object
print('k',k.a,k.b)'''

#Delete static variable from different places

'''class info:
    a=10
    @classmethod
    def k(cls):
        del info.a      #deleting using class name
        #del cls.a       #deleting using cls variable
t=info()
del info.a       #delete static variable outside of the class
info.k()                #we can call class method directly using class name
print(info.__dict__)'''

'''class k:
    a=10
    def __init__(self):
        k.b=20
        del k.a
    def k1(self):
        k.c=30
        del k.b
    @classmethod
    def k2(cls):
        cls.d=40
        del k.c
    @staticmethod
    def k3():
        k.e=50
        del k.d
t=k()            #by calling class through object reference constructor will call a value will be deleted
t.k1()      #by calling instance method b value will be deleted
k.k2()      #by calling class method c value will be be deleted
k.k3()      #by calling static method d value will be deleted
del k.e     #e value will be deleted
print(k.__dict__)'''

#static variable

'''class test:
    @staticmethod
    def average(list1):
        result=sum(list1)/len(list1)  #here result is local variable
        print('Average is: ',result)
    @staticmethod
    def wish(name):
        for i in range(5):        #here i is local variable
            print('Good evening',name)
list1=[10,20,30,40,50]
test.average(list1)
test.wish('Chinmay')'''

#mini program with static variable, instance variable and local variable

'''class Customer:
    This MyBank
    bankname='MyBank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        print('Welcome ',self.name)
        self.balance=self.balance+amount
        print('Your updated balance is: ',self.balance)
    def withdraw(self,amount):
        print('Welcome ',self.name)
        if amount>self.balance:
            print('Insufficient fund')
        else:
            self.balance=self.balance-amount
            print('Your current balance : ',self.balance)
    def money(self):
        print('Welcome ',self.name)
        print('Your Balance is : ',self.balance)
    
print('WELCOME To',Customer.bankname)
name=input('ENTER YOUR NAME ')
c=Customer(name)
while True:
    print('CHOOSE\n d-Deposit\n w-Withdraw\n c-Check Balance\n e-Exit')
    choice=input('Enter your choice ')
    if choice.lower()=='d':
        amount=float(input('Enter amount '))
        c.deposit(amount)
    elif choice.lower()=='w':
        amount=float(input('Enter amount '))
        c.withdraw(amount)
    elif choice.lower()=='c':
        c.money()
    elif choice.lower()=='e':
        print('Thank You For Banking')
        break
    else:
        print('Choose valid option')'''
#grade program

'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hello :',self.name)
        print('Your mark is: ',self.marks)
    def grade(self):
        if self.marks>=60:
            print('First garde')
        elif self.marks>=50:
            print('Second grade')
        elif self.marks>=35:
            print('Third grade')
        else:
            print('Failed')
n=int(input('Enter your no of students : '))
for i in range(n):
    name=input('Enter your name: ')
    marks=int(input('Enter your marks: '))
    s=student(name,marks)
    s.display()
    s.grade()
    print()'''

    #Getter and setter method

'''class Student:
    def setName(self,name):           #setter
        self.name=name
    def getName(self):                #getter
        return self.name
    def setMarks(self,marks):         #setter
        self.marks=marks
    def getMarks(self):               #getter
        return self.marks
n=int(input('Enter number of students: '))
students=[]
for i in range(n):
    s=Student()
    name=input('Enter your name: ')
    marks=int(input('Enter your marks: '))
    print()
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
print(students)
for s in students:
    print('Hello ',s.getName())
    print('Your marks ',s.getMarks())
    print()'''

#Swapping without third variable
'''x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
x=x+y
y=x-y
x=x-y
print('After swapping \n x= ',x,'\ny= ',y)'''

#Swapping using multiplication and division
'''x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
x=x*y
y=x//y         #integer division used
x=x//y
print('After swapping \n x= ',x,'\ny= ',y)'''

#using XOR swapping
'''x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
x = x ^ y
y = x ^ y
x = x ^ y
print('After swapping \n x= ',x,'\ny= ',y)'''

#Function to swapp number
'''def swap(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print('After swapping \n a= ',a,'\nb= ',b)
swap(34,78)'''

#class method 
'''class Bird:
    wings=2
    @classmethod
    def m1(cls,name):
        print('{} flying with {} wings'.format(name,cls.wings))
Bird.m1('Parrot')
Bird.m1('Eagle')'''

# Count no of object
'''class test:
    count=0
    def __init__(self):
        test.count+=1    #it will increament when call class with any object reference
    @classmethod
    def m1(cls):
        print('The no of counts: ',cls.count)
test.m1()
t1=test()
t2=test()
t3=test()
t4=test()
test.m1()'''

#Static method pr Genral utility method
#No use of instance variable and staticc variable
'''class Durgamath:
    @staticmethod
    def add(a,b):
        print('Addition= ',a+b)
    @staticmethod
    def sub(a,b):
        print('Subtraction= ',a-b)
    @staticmethod
    def avg(a,b):
        print('Average= ',a+b/2)
Durgamath.add(10,5)
Durgamath.sub(10,5)
Durgamath.avg(10,5) ''' 

#Instance method , class method and static method
#instance method can call by object reference
#class method can call by object reference or by class name
# static method can call by object reference or by class name
# without decorator we can declare instance method or static method but for class method decrator is mandatory
# if we declare instance variable without self we will get error
'''class test:
    def m1(self):      #we will get error if we will not use self keyword ,it is mandotory as arguement
        print('Hello')
t=test()
t.m1()  '''    # calling by object reference it is instance method 

#Static method without decorator
'''class test:
    def m1():      #without decorator static method implementation can be done
        print('Hello')
test.m1()  '''       #we must call bey class name

#Accessing member of one class inside another class
'''class Employee:
    def __init__(self,enum,ename,esal):
        self.enum=enum
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee no: ',self.enum)
        print('Employee name: ',self.ename)
        print('Employee sal: ',self.esal)
class Manage:
    def salhike(emp):
        emp.esal=emp.esal+10000    #accessing esal the member of employee class
        emp.display()           #accessing display the member of employee class
emp=Employee(100,'Rajesh',40000)
Manage.salhike(emp)
print()
Manage.salhike(emp)'''

#Inner class , class inside another class
#without existing one type of object ,if there is no chance of existing another type of object that is inner class
#it is used for improve modularity and security
'''class Outer:                #outer class
    def __init__(self):
        print('Outer class')
    class Inner:             #inner class
        def __init__(self):
            print('Inner class')
        def m1(self):
            print('Inner class method')
o=Outer()     #1
i=o.Inner()   #2 #by using outer class object creation of inner class object
i.m1()  '''       #we can use one line i=Outer().Inner() by avoiding step 1 & 2 or Outer().Inner().m1()

#Nesting of inner class
'''class Outer:
    def __init__(self):
        print('Outer class')
    class Inner:
        def __init__(self):
            print('Inner class')
        class Nestinner:
            def __init__(self):
                print('Nestinner class')
            def m1(self):   #if it will static metod then object creation not required 
                print('Nest inner method...')   #Outer().Inner().Nestinner.m1() we can call
o=Outer()          #o=Outer().Inner()  or Outer().Inner().Nestinner.m1() will work
i=o.Inner()        #i=o.Nestinner()
j=i.Nestinner()    #i.m1()
j.m1()'''

#Inner class programs
'''class Human:
    class Head:
        def talk(self):  #for this we have to call head
            print('Talking')
        class Brain:
            def think(self):   #for this we have to call brain
                print('Thinking')
hu=Human()
head=hu.Head()
head.talk()
brain=head.Brain()
brain.think()'''

#Smart human program
'''class Human:
    def __init__(self,name):
        print('Human method')
        self.name=name
        self.head=self.Head()   # 1 exec #here head class constructor will execute
    def data(self):
        print('Hello ',self.name)  #3 exec
        print('What about you')    #4 exec
        self.head.talk()       #It will access talk method through head class
        self.head.brain.think()  #It will access think method through brain and head class

    class Head:
        def __init__(self):
            print('Head method')
            self.brain=self.Brain()   #2 exec #here brain class object will execute
        def talk(self):
            print('Talking')        #5 exec

        class Brain:
            def __init__(self):
                print('Brain method')
            def think(self):       
                print('Thinking')  #6 exec
human=Human('Ajit')
human.data()'''

#DOB program
'''class Person:
    def __init__(self,name,dd,mm,yyyy):
        print("Person enter")
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)    #reference to class Dob
    def info(self):
        print('Name ',self.name)
        self.dob.display()  #reference to display method of class dob

    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('Dob enter')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print('DOB : {}/{}/{}'.format(self.dd,self.mm,self.yyyy))
person=Person('Dabb',24,10,1988)
person.info()'''

#Nested methods
'''class test:
    def m1(self):
        def calc(a,b):     #method inside another method
            print('Sum: ',a+b)
            print('Product: ',a*b)
            print('Diference : ',a-b)
            print('Percentage: ',(a+b)/2)
        calc(20,10)
        calc(200,100)
t=test()
t.m1()'''

#Garbage collection
#module is import gc
'''import gc    # garbage collection module
print(gc.isenabled())
gc.disable()   #to disable gc
print(gc.isenabled())
gc.enable()  #to enable gc
print(gc.isenabled())'''

#Destrructor
#It will not destroy the object it only perform clean up activities
'''import time
class test:
    def __init__(self):             #Constructor
        print('Object initialize') 
    def __del__(self):              #Destructor
        print('Fullfilling last wish and performing cleanup activities')
t=test()
t=None
time.sleep(10)
print('End of application')'''

#Every object will destroy after program execution
'''class test:
    def __init__(self):
        print('Object Initialization')
    def __del__(self):
        print('Fullfill the last wish and cleanup')
t1=test()
t2=test()
print('End of execution') ''' #After execution every object will destroy

#Before End of execution
'''class test:
    def __init__(self):
        print('Object Initialization')
    def __del__(self):
        print('Fullfill the last wish and cleanup')
t1=test()
t2=test()
t1=None       #Destructor will execute before execution because it found another object
t2=None
print('End of execution')'''

#Second program
'''import time
class test:
    def __init__(self):
        print('Constructor method')
    def __del__(self):
        print('Destructor executon')
t1=test()
t2=t1
t3=t2
del t1
time.sleep(10)
print('t1 destructed but not object')
del t2
time.sleep(10)
print('t2 destructed but not object')
del t3
time.sleep(10)     #After 3 reference destroyed destruction process will completed
print('End of execution')'''

#Destructor within list
'''import time
class test:
    def __init__(self):
        print('Construction execution')
    def __del__(self):
        print('Destructor execution')
l=[test(),test(),test()]
del l    #destructor will execute after constructor execution
time.sleep(10)
print('End of executon')'''

#Another way
'''import time
class test:
    def __init__(self):
        print('Construction execution')
    def __del__(self):
        print('Destructor execution')
l=[test(),test(),test()]
time.sleep(10)
print('End of executon')    #Destructor will execut after end of execution
time.sleep(10)'''

#Lambda function
'''x = lambda a, b : a * b
print(x(5, 6))'''

#2nd program
'''x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''

#Using member of one class inside another class
#By using Composition or HAS-A relationship
'''class Engine:
    def m1(self):
        print('Engine specific functionality')

class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('Car specific functionality')
        self.engine.m1()
a=Car()
a.m2()'''

#Using instance variable inside another class
'''class Engine:
    def __init__(self):
        self.power='125kw'
    def m1(self):
        print('Engine specific functionality')

class Car:
    def __init__(self):
        self.engine=Engine()     #use of another class
    def m2(self):
        print('Car specific functionality')
        self.engine.m1()
        print(self.engine.power)  #use of instance variable
a=Car()
a.m2()'''

#Second program
'''class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def info(self):
        print('Car namme: {}, Model {}, Color: {}'.format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eid,car):
        self.ename=ename
        self.eid=eid
        self.car=car      #HAS-A relationship
    def einfo(self):
        print('Employee name ',self.ename)
        print('Employee id ',self.eid)
        print('Employee car  info')
        self.car.info()        #Reference to car class
car=Car('Innova','2.8Cresta','White')
emp=Employee('Durga',6767,car)
emp.einfo()'''

#Bubble sort
l=[7,4,2,10,3,1]
for i in l:
    for j in l:
        if(l[j]>l[j+1]):   #not got
            l[j],l[j+1]=l[j+1],l[j]
print('Sorted list',l)

































