# # 
# def greet (name,gender):
#     if gender=='Female':
#         print(f'Hello misss.{name}')
#     else:
#         print(f'Hello mr.{name}')
# greet('ram','male')



# # 
# def salaryIncr(salary):
#     salary+=5000
#     print('hiked salary:',salary)
#     return salary 
# hikedSal=salaryIncr(20000)
# print(hikedSal - 3000)


# # # 
# def square (x):
#     return x**2
# x=eval(input('enter the value'))
# a=square(x)
# print(f'the square of {x} is {a}')


        


###############################################################################################################################################

# #   Function example

#  # 1 waf to perform addition if a>b else perform subtraction
# def num(a,b):
#     if a>b :
#         print(a+b)
#     else:
#         print(a-b)
# num(100,20)


# # 
# def num(a,b):
#     if a>b :
#         return(a+b)
#     else:
#         return(a-b)
# # v=num(a,b)
# v=num(100,20)
# print(v)
                                                                 
                                                                 
# # 2 waf to check that the string is pallindrome or not take user input without using slicing
# def ispal(strr):
#     start=0
#     end=len(strr)-1  
#     while start < end:
#         if strr[start]!=strr[end]:
#             return 'Not pallindrome'
#         start+=1
#         end-=1 
#     return'Pallindrome'
# print(ispal('momo'))        


# # 3  waf to return the square, cube, square root, cube root of a value taken from user
# def value(x):
#     return x**2 , x**3, x*(0.5), x**(1/3)
# v=(value(eval(input('enter the value:'))))
# print(v)


# # # 4 "WAF to search for a particular character in a given string both of them should be taken from user as an argument and print the index of character."
# def check (strr,chrr):
#     for i in range (len (strr)):
#         if strr[i]==chrr:
#             return i
#     return -1
# res=check('malayalam','a')
# if res != -1:
#     print(res)
# else:
#     print('Not found in the given string')
    
    
# # 5 waf to take the square of all the elements present inside the list
# def num(x):
#     return [i**2 for i in x]
# x=eval(input('enter the value:'))
# v=num(x)
# print(v)


# # 6 waf to fetch the last digit of a number after performingthe addition of two number
# def last_digit_after_addition(a, b):
#     total = a + b
#     last_digit = total % 10
#     return last_digit
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = last_digit_after_addition(a, b)
# print(f"The last digit of the sum of {a} and {b} is: {result}")


# # 7 waf to take 3 numbers from user and find the sum of first two and substract the third number from the result of addition
# def num(a,b,c):
#     return (a+b)-c
# a=eval(input('enter the value:'))
# b=eval(input('enter the value:'))
# c=eval(input('enter the value:'))
# v=num(a,b,c)
# print(v)


# # 8 waf to check that the given character is a special character alphabet or a digit without inbuilt function
# def char(x):
#     code = ord(x)
#     if 48 <= code <= 57:   
#         return 'digit'
#     elif (65 <= code <= 90) or (97 <= code <= 122):  # A-Z or a-z
#         return 'alphabet'
#     else:
#         return 'special character'
# ch = input("Enter a single character: ")
# result = char(ch)
# print(f"The character '{ch}' is a {result}.")
 

#######################################################################################################################

# # 1.Function to print Hello
# def name(a):
#     return a
# b=name('hello')
# print(b)


#2. Function to add two numbers
# def num(a,b):
#     return a+b
# b=num(5,6)
# print(b)


# # 3. Function to subtract two numbers
# def num(a,b):
#     return (a-b)
# c=num(100,20)
# print(c)
    

# # 4.Write a function to find the square of a number
# def squre(a):
#     return (a*a)
# c=squre(5)
# print(c)


# # 5.Write a function to find the cube of a number.
# def cube(a):
#     return(a**a)
# c=cube(3)
# print(c)


# # 6.Write a function to check whether a number is even or odd.
# def num(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# c=num(50)
# print(c)


# # 7.Write a function to check whether a number is positive or negative.
# def num(a):
#     if 0<=a<=9:
#         return 'positive'
#     else:
#         return 'negative'
# c=num(5)
# print(c)


# # 8.Write a function to find the largest of two numbers.
# def num():
#     a=int(input('enter the num'))
#     b=int(input('enter the num'))
#     c=int(input('enter the num'))
#     if a>b and a>c:
#         return (a)
#     elif b>a and b>c:
#         return (b)
#     else:
#         return (c)
# v=num()
# print(v)  


# # 9.Write a function to find the factorial of a number.
# def factorial(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     return fact
# c=factorial(5)
# print(c)
        

# # 10.Write a function to check whether a number is prime.
# def prime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return "Prime"
#     return "Not Prime" 
# print(prime(13)) 


########################################################################################################################

# def welcome():
#     print('Welcome to Python')
# welcome()


# def add(a, b):
#     print(a + b)

# add(10, 20)


# def student(name, age, city):
#     print(name)
#     print(age)
#     print(city)

# student("Prajwal", 22, "Navi Mumbai")



# def add(a,b):
#     print(a*b)
# add(10,20)


# def stud(name,age):
#     print(name,age)
# stud('Prqjwal' , 21)



# def don(name,sal,dept):
#     print(name,sal,dept)
# don('Prajwal',2000,20)


# def st(name,age):
#     print(name,age)
# st(name='prajwal', age=20)


# def emp(name,sal,dept):
#     print(name,sal,dept)
# emp(name='praj',sal=200,dept='it')


# def ad(a,b):
#     print(a+b)
# ad(b=20,a=5)


# def s(name,age=20):
#     print(name,age)
# s('Prajeal')


# def greet(name, mess='hello'):
#     print(name,mess)
# greet('prajwal','hii')



# def pro(name,price,qualitity=1):
#     print(price)
# pro('prajeal',2000)


# def t(name,dept,sal=200):
#     print(name,dept,sal)
# t('prawja',dept='it')



# def employee(name, salary, department):
#     print(name, salary, department)
# employee(department='it',salary=1000,name='prajwal')



# def product(name, price, quantity=1):
#     print(name, price, quantity)
# product('prajwal',price=200,quantity=2)



# def add(a,b):
#     return(a+b)
# x=add(10,20)
# print(x)


# def squ(a):
#     return a**2
# p=squ(5)
# print(p)


# def add(a,b):
#     return(a*b)
# x=add(10,20)
# print(x)


# def gret(a,b):
#     if a<b:
#         return b
#     else:
#         return a
# p=gret(105,20)
# print(p)


# def to(m1,m2,m3):
#     return(m1+m2+m3)
# a=to(10,20,30)
# print(a)


# def s(a,b):
#     return a+b , a-b
# p,t=s(10,30)
# print(p)
# print(t)


# def mu(a,b):
#     return a+b ,a-b , a*b
# a,s,m=mu(10,20)
# print(a)
# print(s)
# print(m)


# def nm(name,marks):
#     return(name,marks)
# a=nm('prajal', 30)
# print(a)


# def sc(a):
#     return a*a , a**3
# a,c=sc(5)
# print(a)
# print(c)


# def m(a,b,c):
#     if b<a and c<a:
#         return(a)
#     elif a<b and c<b:
#         return(b)
#     elif a<c and b<c:
#         return(c)
# t=m(5,6,7)
# print(t)



# def pn(a):
#     if 0<a:
#         return('positiv')
#     else:
#         return('negative')
# t=pn(522)
# print(t)


# def eo(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# t=eo(6)
# print(t)


# def age(a):
#     if a>18:
#         return('adult')
#     else:
#         return ('not adual')
# t=age(8)
# print(t)


# def m(a):
#     if a>=40:
#         return 'pass'
#     else:
#         return 'fail'
# t=m(20)
# print(t)


# def c(a,b):
#     return a+b
# t=c(5,5)
# print(t+10)


# def s(a):
#     return a*a
# t=s(5)
# print(t*5)


# def c(a,b):
#     return a+b
# t=c(5,5)
# print(t*t)


# def ma(m1,m2,m3):
#     return m1+m2+m3


# def per(t):
#     return t/3
# t=ma(50,60,40)
# y=per(t)
# print(y)


# def ap():
#     x=100
#     print(x)
# ap()


# def na():
#     name='prajwal'
#     return name
# p=na()
# print(p)



# def d(a,b):
#     result=a+b
#     return result
# t=d(10,20)
# print(t)


# def d():
#     x=10+20
#     return x
# t=d()
# print(x)


# def a():
#     x=10
#     return x
# t=a()
# print(t) 


# def a():
#     x=20
#     return x
# t=a()
# print(t) 


# x = 10
# def test():
#     global x
#     x = 20
# test()
# print(x)


# x=100
# def a():
#     print(x)
# a()

# a='prajwal'
# def i():
#     print(a)
# i()


# x=10
# def o():
#     global x
#     x=50
#     return x
# t=o()
# print(x)


# count=0
# def u():
#     global count
#     count=1
#     return count
# t=u()
# print(t)


# # Q5
# x = 100
# def test():
#     x = 50
#     print("Local:", x)
# test()
# print("Global:", x)


# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#     inner()
#     print(x)
# outer()


# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()
# outer()


# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#         print(x)
#     inner()
# outer()


# def outer():
#     def inner():
#         print('hello python')
#     inner()
# outer()


# def cal():
#     def add(a,b):
#         return a+b
#     t=add(10,20)
#     print(t)
# cal()


# def stu():
#     def marks(m1,m2,m3):
#         return m1+m2+m3
#     t=marks(10,20,30)
#     print(t)
# stu()


# def count(a):
#     if a < 1:
#         return
#     print(a)
#     count(a-1)
# count(5) 


# def count(n):
#     if n > 5:
#         return 
#     print(n)
#     count(n + 1)
# count(1)


# def ev(a):
#     if a > 10:
#         return
#     elif a%2==0:
#         return a
#     print(a)
#     ev(a+1)
# ev(1)


# def ev(a):
#     if a > 10:
#         return
#     ev(a+2)
#     print(a)
# ev(0)


# def odd(a):
#     if a > 10:
#         return
#     elif a%2==1:
#         print(a)
#     odd(a+1)
# odd(1)


# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)
# result = total(5)
# print(result)


# def num(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# t=num(10,20,30)
# print(t) 


# Ek function maximum() banao jo *args use kare aur multiple numbers mein se maximum number return kare.
# def max(*a):
#     for i in a:
#         if i<a:
#             print(i)
# max(10,20,30)


# def maximum(*args):
#     max_num = args[0]
#     for i in args:
#         if i > max_num:
#             max_num = i
#     return max_num
# t = maximum(10, 50, 20, 80, 30)
# print(t)

# def avg(*a):
#     total=0
#     count=0
#     for i in a:
#         count+=1
#         total+=i
#     return total / count
# t=avg(40,50,60)
# print(t)


# def min(*a):
#     min_no=a[0]
#     for i in a:
#         if i < min_no:
#             min_no=i
#     return min_no
# t=min(10,2,3,2,8)
# print(t)


# def even(*a):
#     count=0
#     for i in a:
#         if i%2==0:
#             count+=1
#     return count
# t=even(10,20,30,41,50)
# print(t)


# def odd(*a):
#     total=0
#     for i in a:
#         if i%2!=0:
#             total+=i
#     return total
# t=odd(1,3,9,8,4,0)
# print(t)


# def stu(**a):
#     return a
# t=stu(name="Prajwal", age=20, city="Mumbai")
# print(t)


# def emp(**a):
#     for i,j  in a.items():
#         print(j) 
# t=emp(name="Prajwal", age=20, salary=25000) 


# def emp(**a):
#     for i , j in a.items():
#         print()
# emp(name="Prajwal", age=20, salary=25000)


# def emp(**a):
#     return a["name"]
# t = emp(name="Prajwal", age=20, salary=25000)
# print(t)

# def stu(**a):
#     return a['course'],a['name']
# t=stu(name="Prajwal", age=20, course="MCA", city="Mumbai")
# print(t)


# def emp(**a):
#     t=a['salary']
#     p=a['bonus']
#     total=t+p
#     print(total) 
# emp(name="Prajwal", salary=25000, bonus=5000)


# def even(**a):
#     count=0
#     for i , j in a.items():
#         if j%2==0:
#             count+=1
#     return count
# t=even(a=10, b=21, c=30, d=45, e=50)
# print(t)


# def name(*a):
#     total=0
#     for i in a:
#         if type(i) == int:
#             total+=i
#         else:
#             print(i)
#     return total
# t=name("Prajwal", 10, 20, 30)
# print(t)


# def avg(name,*a):
#     count=0
#     total=0
#     for i in a:
#         count+=1
#         total+=i
#     print(name) 
#     return total / count
# t=avg("Prajwal", 10, 20, 30, 40)
# print(t)


# def stu(name,**a):
#     return name , a['age'],a['city'] ,a['course']
# s=stu("Prajwal", age=20, city="Mumbai", course="MCA")
# print(s)


# def even(**a):
#     total=0
#     for i in a.values():
#         if i%2==0:
#             total+=i
#     return total
# t = even(a=10, b=21, c=30, d=45, e=50)
# print(t)


# def min(**a):
#     mi=None
#     for i in a.values():
#         if mi is None or mi > i:
#             mi=i
#     return mi
# t=min(o=10, b=50, c=20, d=5, e=40)
# print(t)


# def fact(a):
#     if a==1:
#         return 1
#     return a * fact(a-1)
# t=fact(6)
# print(t)


# def rec(a):
#     if a<1:
#         return
#     print(a)
#     rec(a-1)
# rec(10)


# lambda a: a*a
# print(5)

# print ((lambda a,b : a*b)(10,20))


# s=lambda a,b,c: if b>a and c>a print()

# print((lambda a, b, c:   a if a > b and a > c    else b if b > c and b > a  else   c)(10, 25, 15)) 

# n = [1, 2, 3, 4, 5]
# num=lambda n: [i*i for i in n]
# print(num(n))

# a=(10, 20, 30)
# num=lambda a: [count=0 total=0 total+=i count+=1 total/count for i in a]
# print(num(a))


# numbers = [1, 2, 3, 4, 5]
# re=[i*i for i in numbers]
# print(re)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# re=[ i for i in numbers if i%2==0]
# print(re)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# re=[i for i in numbers if i%2!=0]
# print(re)


# numbers = [1, 2, 3, 4, 5, 6]
# re=[i*i for i in numbers if i%2==0]
# print(re)


# names = ["prajwal", "amit", "rohan", "raj"]
# re=[i.upper() for i in names]
# print(re)


# numbers = [10, 15, 20, 25, 30, 35]
# re=[i for i in numbers if i>20]
# print(re)

# numbers = [1, 2, 3, 4, 5, 6]
# re=[ i*i if i%2==0 else i**3 for i in numbers ]
# print(re)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# re=[i  for i in numbers if i%3==0]
# print(re)


# names = ["ram", "amit", "rohan", "raj", "suresh"]
# re=[names[i] for i in range(len(names)) if len(names[i]) >4]
# print(re)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# re=[i+i for i in numbers if i > 20]
# print(re)

# numbers = [1, 2, 3, 4, 5, 6]
# re=[i+10 for i in numbers ]
# print(re)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# re=['even' if i%2==0  else 'odd' for i in numbers  ]
# print(re)


# numbers = [2, 5, 8, 11, 14, 17, 20]
# re=[i*i if i%2==0  else i+i   for i in numbers]
# print(re)

# numbers = [5, 10, 15, 20, 25, 30]
# re=[i**3 for i in numbers if i < 20]
# print(re)


# matrix = [[1, 2], [3, 4], [5, 6]]
# a=[]
# re= [j for i in matrix for j in i ]
# print(re)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# re=[ j*j for i in matrix for j in i if j%2==0]
# print(re)


# numbers = [1, 2, 3, 4, 5, 6]
# re={i*i for i in numbers }
# print(re)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# re={i for i in numbers if i%2==0}
# print(re)


# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# re={i*i for i in numbers}
# print(re)


# names = ["ram", "amit", "rohan", "raj", "ram", "amit"]
# re={ len(i) for i in names }
# print(re)


# numbers = [10, 15, 20, 25, 30, 35, 40]
# re={i/2 for i in numbers if i > 20 }
# print(re)


# names = ["ram", "amit", "rohan", "raj", "suresh", "om"]
# re={ len(i) for i in names if len(i)>4}
# print(re)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# re={ i*i if i%2==0 else i*i*i for i in numbers}
# print(re)


# data = [[1, 2], [2, 3], [3, 4]]
# re={i for i in data for j in i}
# print(re)

# words = ["apple", "banana", "apple", "mango", "banana", "kiwi"]
# re={i for i in words if len(i)>=5}
# print(re)

# numbers = [1, 2, 3, 4, 5]
# re={i:i*i for i in numbers}
# print(re)


# numbers = [10, 15, 20, 25, 30]
# re={i:i+i for i in numbers if i%2==0}
# print(re)

# names = ["Ram", "Amit", "Rohan", "Raj", "Prajwal"]
# re={i:i[0] for i in names}
# print(re)

# numbers = [5, 10, 15, 20, 25, 30]
# re={i:'even'if i%2==0 else 'odd' for i in numbers }
# print(re)

# words = ["apple", "cat", "banana", "dog", "mango"]
# re={i:len(i) for i in words if len(i)>=5}
# print(re)

# numbers = [1, 2, 3, 4, 5]
# re={i:'possit' if i%2==0 else 'negative' for i in numbers}
# print(re)

# names = ["Ram", "Amit", "Rohan", "Raj"]
# re={i[0]:i for i in names}
# print(re)


# numbers = [1, 2, 3, 4, 5]
# result = (i*i for i in numbers)
# print(result)

# numbers = [10, 15, 20, 25, 30]
# re=(i for i in numbers if i%2==0)
# for i in re:
#     print(i)


# numbers = [10, 15, 22, 31, 40, 55, 60, 73]
# re=(i for i in numbers if i%2==0 and i>20)
# for i in re:
#     print(i)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# re=(i*2 if i%2==0 else i*3 for i in numbers)
# for i in re:
#     print(i)

# numbers = [10, 23, 42, 55, 68, 71, 80, 91]
# re=(i*i  if i%2==0 and i>50 else i*3 for i in numbers)
# for i in re:
#     print(i)

# numbers = [12, 17, 24, 31, 40, 53, 60, 71]
# re=(i/2 if i%2==0 else i+i for i in numbers if i>20)
# for i in re:
#     print(i)


# numbers = [1, 2, 3, 4, 5]
# re=lambda i : i*i 
# for i in numbers:
#     print(re(i))


# a=lambda a, b: a if a>b else b
# print(a(10,5))

# a=lambda a, b, c: a if b<a and c<a else b if a<b and c<b else c
# print(a(10,20,60))

# a=lambda a: 'even' if a%2==0 else 'odd'
# print(a(6))

# a=lambda a: a.upper()
# print(a('pradjsn'))

# a=lambda a :  a%3==0 and a%5==0
# print(a(5))

# p=lambda a,b,c : a if b>a and c>a else b if a>b and c>b else c
# print(p(10,20,30)) 

# a=lambda a: 'palandrom' if a==a[::-1] else 'not palandrom'
# print(a('omol'))

# names = ["ram", "amit", "rohan"]
# result = map(lambda x: x.upper(), names)
# print(list(result))

# numbers = [2, 4, 6, 8, 10]
# re=map(lambda x: x*x,numbers)
# print(list(re))

# names = ["ram", "amit", "rohan", "prajwal"]
# re=map(lambda x: x.upper(),names)
# print(list(re))

# numbers = [10, 20, 30, 40, 50]
# re=map(lambda x: x+10 , numbers)
# print(list(re))

# numbers = [5, 10, 15, 20, 25]
# re=map(lambda x: x*2 if x%2==0 else x*3,numbers)
# print(list(re))

# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# re=map(lambda x: len(x),names)
# print(list(re))


# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# re=map(lambda x : 'hello '+x, names)
# print(list(re))


# numbers = [2, 4, 6, 8, 10]
# def seq(x):
#     return x*x
# re=map(seq,numbers)
# print(list(re))


# names =  [10, 25, 40, 55, 70]
# def add(a):
#     if a>50:
#         return(a+10)
#     else:
#         return (a-5)
# re=map(add,names)
# print(list(re))


# numbers = [10, 15, 20, 25, 30, 35]
# re=filter(lambda x: x%2==0 , numbers)
# print(list(re))

# numbers = [5, 12, 18, 25, 30, 41, 50]
# re=filter(lambda x: x%5==0 and x>20, numbers)
# print(list(re))


# names = ["Ram", "Amit", "Rohan", "Prajwal", "Om"]
# re=filter(lambda x : len(x)>4,names)
# print(list(re))


# names = ["Ram", "Amit", "Rohan", "Prajwal", "Om", "Ankit"]
# re=filter(lambda x : x[0]=='A' , names)
# print(list(re))


# students = {
#     "Rahul": 75,
#     "Amit": 45,
#     "Rohan": 82,
#     "Prajwal": 35,
#     "Neha": 90
# }
# re=filter(lambda x : students[x]> 50 , students)
# print(list(re))


# data = (10, "Python", 25, "Java", 40, "SQL", 55)
# re=filter(lambda x : type(x)==int , data)
# print(list(re))

# names = ["Ram", "Amit", "Rohan"]
# marks = [80, 75, 90]
# re=zip(names,marks)
# print(list(re))

# names = ["Ram", "Amit", "Rohan"]
# ages = [20, 21, 22]
# cities = ["Mumbai", "Pune", "Nashik"]
# re=zip(names,ages,cities)
# print(list(re))

# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# marks = [75, 45, 82, 35]
# re=filter(lambda x: x>50 ,marks)
# om=zip(names,re)
# print(list(om))

# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# marks = [75, 45, 82, 35]
# p=zip(names,marks)
# # re=map{lambda x , j : names ,marks}
# print(list(p))


# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# marks = [75, 45, 82, 35]
# data=zip(names,marks)
# re= filter(lambda x: x[1]>50 , data)
# result = map(lambda x: x[0] + " scored " + str(x[1]), re)
# print(list(result))

# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# for i , j in enumerate(names):
#     print(i,j)

# names = ["Ram", "Amit", "Rohan", "Prajwal"]
# for i , j in enumerate(names):
#     print(i,j)

# numbers = [10, 15, 20, 25, 30]
# re=all(x>5 for x in numbers)
# print(re)

# def greet():
#     print("Hello")
# x = greet
# x()

# def welcome():
#     print("Welcome to Python")
# a=welcome
# a()

# def add():
#     print(10 + 20)
# x=add
# x()

# def message():
#     print("Hello Python")
# a=message
# a()

# def double(x):
#     return x * 2
# def process(func, number):
#     return func(number)
# re=process(double,5)
# print(re)

# def square(x):
#     return x * x

# def calculate(func, number):
#     return func(number)
# re=calculate(square,7)
# print(re)

# def outer():
#     def inner():
#         print("Python")
    
#     return inner
# a=outer()
# a()

# def cube(x):
#     return x * x * x

# def calculate(func, number):
#     return func(number)
# re=calculate(cube,4)
# print(re)

# def outer():
#     message = "Hello"

#     def inner():
#         print(message)

#     return inner
# re=outer()
# re()

# def outer():
#     x = 5
#     def inner():
#         print(x * 2)
#     return inner
# re=outer()
# re()

# def outer():
#     x = 10
#     def inner():
#         return x + 5
#     return inner
# re=outer()
# print(re())

# def outer():
#     name = "Prajwal"
#     def inner():
#         return "Hello " + name
#     return inner
# re=outer()
# print(re())

# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper
# @decorator
# def message():
#     print("Hello Python")
# message()

# def om(don):
#     def wrap():
#         print('starting')
#         don()
#         print('ending')
#     return wrap
# @om
# def mam():
#     print('prajwal')
# mam()


# def dec(so):
#     def wrap():
#         print('before')
#         so()
#     return wrap
# @dec
# def com():
#     print('welcome')
# com()

# def cal(fun):
#     def wrap(*args, **kwargs):
#         print('Calculating')
#         res=fun(*args,**kwargs)
#         return res
#     return wrap
# @cal
# def om(a,b):
#     return a+b
# print(om(10,30))

# def oo(fun):
#     def wrap(*a,**kw):
#         print('Function')
#         re=fun(*a,**kw)
#         return re
#     return wrap
# @oo
# def mul(a,b):
#     return a*b
# print(mul(10,20)) 


# def dec1(fun):
#     def wrap():
#         print('1')
#         fun()
#     return wrap
# def dec2(fuc):
#     def wrap2():
#         fuc()
#         print('2')
#     return wrap2
# @dec1
# @dec2
# def hello():
#     print('hellow')
# hello()

# def dec1(fun):
#     def wrap():
#         res= fun()
#         return res.upper()
#     return wrap
# def dec2(fun):
#     def wrap2():
#         ret= fun() 
#         return ret + ' python'
#     return wrap2
# @dec1
# @dec2
# def mass():
#     return('hello')
# print(mass())

# def dec1(fun):
#     def wrap():
#         print('start')
#         fun()
#     return wrap
# def desc2 (fun):
#     def wrap2():
#         fun()
#         print('End')
#     return wrap2
# @dec1
# @desc2
# def test():
#     print ('running')
# test()

# def dec1(fun):
#     def wrap1():
#         print('login')
#         fun()
#     return wrap1
# def desc2(fun2):
#     def wrap1():
#         print('assc')
#         fun2()
#     return wrap1
# @dec1
# @desc2
# def das():
#     print( 10+20)
# das()

# def multiply(a: int, b: int) ->int:
#     return a * b
# print(multiply(10,20))

# def greet(name:str)-> str:
#     return 'hello'+" "+ name
# print(greet('prajwal'))

# def avg(a:float, b:float):
#     return (a+b)/2
# print(avg(10.5,20.5))

# def ev(a:int)->bool:
#     if a%2==0:
#         print(True)
#     else:
#         print(False)
# ev(101)

# name :str='praj'
# age :int =20
# sal :float = 20.2
# print(name)
# print(age)
# print(sal)

# def squ(a:int)->int:
#     return a*a
# print(squ(5))

# def avg(a:list[int])->float:
#     return sum(a)/len(a)
# print(avg([80, 75, 90, 85]))

# def get(name:list[str])->list[str]:
#     return [i for i in name if len(i)>5]
# print(get(["Ram", "Prajwal", "Amit", "Rohan"]))

# def ge(na:list[int])->list[int]:
#     return [i for i in na if i%2==0]
# print(ge([10, 15, 20, 25, 30]))

# def om(name:str,age:int,mark:float)->dict:
#     return {'n':name,'a':age,'m':mark}
# print(om('pra',5,52.2))

# def cal(a:list[int])->float:
#     return [i+i for i in a]
# print(cal([100.5, 200.0, 50.5]))

# def add(a,b):
#     """ add a two number"""
#     return a+b
# print(add(10,20))
# print(add.__doc__)

# def amdd(a,b):
#     """ add a two number"""
#     return a*b
# print(amdd(10,20))
# print(amdd.__doc__) 

# if __name__ == "__main__":
#     print("Program started")
  
# print(__name__)

# def sq(a):
#     """ this is square"""
#     return a*a
# print(sq.__doc__)

# def test():
#     print(callable(test))
# test()

# t='ds'
# print(callable(t))

# def add(a,b ,/):
#     return a+b
# print(add(10,20))

# def stu(name,age , /, ds ):
#     return name, age ,ds
# print(stu('pdhj',52,ds='sf'))