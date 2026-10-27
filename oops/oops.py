
# # #
# class Python:
#     a=50
#     b=20
# ob1=Python()
# ob2=Python() 
# ob1.a=40
# ob1.b=35
# Python.a=12
# print(ob1.a,ob1.b)
# print(ob2.a,ob2.b)


# # #
# class Python:
#     a=50
#     b=20
# ob1=Python()
# ob2=Python() 
# ob1.a=40
# ob1.b=35
# Python.a=12
# print(ob1.a,ob1.b)
# print(ob2.a,ob2.b)


# #
# class Python:
#     a=50
#     b=20
# ob1=Python()
# ob2=Python() 
# ob1.a=40
# ob1.b=35
# Python.a=12
# print(ob1.a,ob1.b)
# print(ob2.a,ob2.b)


# # #
# class Python:
#     a=50
#     b=20
# ob1=Python()
# ob2=Python() 
# ob1.a=40
# ob1.b=35
# Python.a=12
# print(ob1.a,ob1.b)
# print(ob2.a,ob2.b)

# #####################################################################################################
# 1)
# class Student:
#     def set_name(self, name):
#         self.name = name
# s1 = Student()
# s1.set_name("Prajwal")
# print(s1.name)

# 2)
# class stud():
#     def set_data(self,name,age):
#         self.nav=name
#         self.vay=age
# s1=stud()
# s2=stud()
# s1.set_data('prajwal',36)
# s2.set_data('ram',25)
# print(s1.nav,s1.vay)
# print(s2.nav,s2.vay)

# 3)
# class car():
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
# m1=car('martr', 'forc',2000)
# m2=car('mom','asf',25689)
# print(m1.model,m1.brand,m1.price)
# print(m2.model,m2.brand,m2.price)

# ######################
# ############# Parameterized constructor
# 1)
# class bankaccount():
#     def __init__ (self, account_holder,account_number,balance):
#         self.ah=account_holder
#         self.an=account_number
#         self.b=balance
#     def deposit_ammout(self,amount):
#         self.b = self.b + amount
#     def withdrow (self, bonus):
#         self.b = self.b - bonus
# a=bankaccount('prajwal',12345,10000)
# a.deposit_ammout(5000)
# a.withdrow(3000)
# print(a.ah,a.an,a.b)

# 5)
# class student():
#     def __init__(self,name,m1,m2,m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def total(self):
#         self.tmarks = self.m1 + self.m2 + self.m3 
#     def per(self):
#         self.persent=(self.tmarks/300)*100
# vo=student('prajwal',50,50,50)
# vo.total()
# vo.per()
# print('name',vo.name)
# print('total',vo.tmarks)
# print('prcentag',vo.persent)   

# 2)
# class employe():
#     def __init__(self,name,salary,bonase):
#         self.name=name
#         self.salary=salary
#         self.bonase=bonase
#     def final_sal(self):
#         return self.salary+self.bonase
# em=employe('prajwal',20000,5000)
# print('name=',em.name)
# print('salary=',em.salary)
# print('bonase=',em.bonase)
# print('total sal=',em.final_sal())

# # ############# non-parameterized constructor
# 1)
# class car():
#     def __init__(self):
#         self.brand='bmw'
#         self.model='papa'
#         self.price=12358
# m=car()
# print(m.brand,m.model,m.price)


# class mobail():
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
# a1=mobail('oppo',20520)
# a2=mobail('apple',123365)
# print(a1.price,a1.brand)
# print(a2.price,a2.brand)


class Student:
    def __init__(self):
        self.name = "Prajwal"
s1=Student()
print(s1.name)