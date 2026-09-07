# # 1 Positive, Negative ya Zero
# a=int(input('enter number'))
# if a>=1:
#     print('positive')
# elif a<0:
#     print("nagativa")
# elif a==0:
#     print("zero")
    
    
# # 2 Vote dene ki age check karo
# a=int(input('enter number'))
# if a<18:
#     print("not eligibal")
# elif a>=18:
#     print('eligibal')
    

# # 3 Password check karo
# a=(input('enter the password'))
# if a=="prajwal":
#     print('correct pass')
# else:
#     print('not crrect')


# # 4 Sab se bara number (2 numbers me)
# a=int(input('enter no'))
# b=int(input('enter no'))
# if a<b:
#     print("b is big no")
# else:
#     print("a is big no")
    

# # 5 Grade system
# a=int(input("enter value"))
# if a>=90:
#     print("a")
# elif a>=80:
#     print("b")
# elif a>=70:
#     print("c")
# elif a>=60:
#     print("d")
# else:
#     print('fail')

# --------------------------------------------------------------------------------------------------------------------------

# practise start - (1-9-2026)

# Simple If qutions: 


# # 1. Wap to print the square of a number only if it is even. 
# a=int(input("enter number"))
# if a%2==0:
#     print( a**2)

# # 2. Wap to check whether the character is vowel or not. 
# a=input('enter the value: ')
# if a in 'aeiou':
#     print('vowel')

# # 3. Wap to print Ascii value of a character only if it is upper case. 
# a=input('enter the value: ')
# if 'A'<=a<='Z':
#     print(ord(a)) 

# # 4. Wap to print the cube of a number only if it is divisible by 9 or 6. 
# a=int(input('enter the value: '))
# if a%9==0 and a%6==0:
#     print(a**3)

# # 5. Wap to check whether the given integer is 3 Digit number. 
# a=int(input('enter the value: '))
# if 100<=a<=999:
#     print(a)

# # 6. Wap to check whether the last digit of a given number is 5. 
# a=int(input('enter the value: '))
# if a % 10 ==5 :
#     print(a)

# # 7. Wap to check whether the given data is float.
# a=float(input('enter the value: '))
# if type(a)==float:
#     print(a)

# # 8. Wap to check whether the data is single value data. 
# a=(input('enter the value: '))
# if type(a) in (int,str,float):
#     print('single value')

# # 9. Wap to check whether the given character is digit or not. 
# a=(input('enter the value: '))
# if 'a'<=a<='z' or 'A'<=a<='Z':
#     print('not digit')

# # 10. Wap to check whether the given integer is multiple of 3. 
# a=int(input('enter the value: '))
# if a%3==0:
#     print("Multiple of 3")


# -----------------------------------------------------------------------------------------------------------------

# # If else qution :

# # 11. Wap to check whether the data is mutable or not. 
# a= eval(input('enter the value: '))
# if type(a) in (list,set,dict):
#     print('mutable datatype')
# else:
#     print('immutable')

# # 12. Wap to check whether the given character is digit or not. 
# a= (input('enter the value: '))
# if 'a'<=a<='z' or 'A'<=a<='Z':
#     print( 'notdigit')
# else:
#     print('digit')

# # 13. Wap to check whether the given character is special or not. 
# a= (input('enter the value: '))
# if a in '&$#@':
#     print('special')
# else:
#     print('not spaciel')

# # 14. Wap to check whether a list consists of middle value or not. 
# a= eval(input('enter the value: '))
# if len(a)%2==1:
#     print('mid value')
# else:
#     print('not mid value')

# # 15. Wap to check whether the number is even or odd. 
# a= eval(input('enter the value: '))
# if a%2==0:
#     print('even')
# else:
#     print('odd')

# # 16. Wap to check whether the given data is mutable or immutable. 
# a= eval(input('enter the value: '))
# if type(a) in (list,set,dict):
#     print('mutable')
# else:
#     print('immutable')

# # 17. Wap to check whether 2 values are pointing to the same memory or not. 
# a = [10, 20, 30]
# b = a
# if a is b:
#     print("Both are pointing to the same memory")
# else:
#     print("Both are not pointing to the same memory")

# # 18. Consider a tuple of length 2 and check whether the tuple is homogenous or not. 
# a = (10, 20)
# if type(a[0])==type(a[1]):
#     print('homogenous')
# else:
#     print('not homo')

# # 19. Wap to check whether the string is palindrome or not. 
# a= (input('enter the value: '))
# if a==a[::-1]:
#     print('palindrome')
# else:
#     print('not palin')

# # 20. Wap to check whether the number is positive or negative. 
# a= int(input('enter the value: '))
# if 1<=a<=9 :
#     print('positive')
# else:
#     print('negative')


# ---------------------------------------------------------------------------------------------------------------------------

# # If else Elif qution : (2-9-2026)


# # 21. Wap to check whether the char is uppercase, lowercase, digit or special char. 
# a= (input('enter the value: '))
# if 'a'<=a<='z' :
#     print('lowercase')
# elif 'A'<=a<='Z':
#     print('uppercase')
# elif '0'<=a<='9' :
#     print(type('digit'))
# else:
#     print('specail char')


# # 22. Wap to check whether the given integer is single digit or two digits or three digits or more than three digits. 
# a= int(input('enter the value: '))
# if -9<=a<=9 :
#     print('single digit')
# elif -99<=a<=99:
#     print('two sum')
# elif -999<=a<=999:
#     print('three digit')
# else:
#     print('more than three')

# # 23.Wap to check the given points are lying in which quadrant. 
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# if x > 0 and y > 0:
#     print("First Quadrant")
# elif x < 0 and y > 0:
#     print("Second Quadrant")
# elif x < 0 and y < 0:
#     print("Third Quadrant")
# elif x > 0 and y < 0:
#     print("Fourth Quadrant")
# else:
#     print("Point lies on X-axis, Y-axis or Origin")

# # 24. Wap to find the greatest of 3 numbers. 
# a= int(input('enter the value: '))
# b= int(input('enter the value: '))
# c= int(input('enter the value: '))
# if a<=b and c<=b:
#     print('b:',b)
# elif b<=a and c<=a:
#     print('a:',a)
# else:
#     print('c:',c)

# # 25. Wap to find the smallest of 3 numbers. 
# a= int(input('enter the value: '))
# b= int(input('enter the value: '))
# c= int(input('enter the value: '))
# if a>=b and c>=b:
#     print('b:',b)
# elif b>=a and c>=a:
#     print('a:',a)
# else:
#     print('c:',c)

# # 26.Wap to check the relation between two integer numbers. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a == b:
#     print("Both numbers are equal")
# elif a > b:
#     print("First number is greater")
# else:
#     print("Second number is greater")

# # 27. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, 
# # if it is digit print the reminder when  it is divided by 3 else if it is special character print it’s ASCII value. 
# a = (input("Enter first number: "))
# if 'a'<=a<='z':
#     print((chr(ord(a)-32)))
# elif 'A'<=a<='Z':
#     print(a.lower())
# elif '0' <= a <= '9':
#     print(int(a) % 3)
# else:
#     print(ord(a))


# # 28.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ 
# # if the number is multiple of both 3 and 5. 
# a = int(input("Enter first number: "))
# if  a%3==0 and a%5==0:
#     print('Fizzbuzz')
# elif a%5==0:
#     print('buzz')
# elif a%3==0:
#     print('fizz')
# else:
#     print(a)


# -----------------------------------------------------------------------------------------------------------------------

# Nested if: 


# # 29.Wap to login into the Instagram with valid username and password.(enter password only if the user name is valid) 
# username=input('enter the user name: ')
# if username=='admin':
#     password=input('enter the password : ')
#     if password=='p123':
#         print('login')
#     else:
#         print('wring password')
# else:
#     print('user name not correct')


# # 30. Wap to print the middle value of a list only if it is string. 
# a = [10, "pra", 30]
# middle = len(a) // 2
# if len(a) % 2 != 0:
#     if type(a[middle]) == str:
#         print(a[middle])


# # 31.Wap to check whether the character is vowel or consonant. 
# a=(input('enter the user name: '))
# if 'a'<=a<='z' or 'A'<=a<='Z':
#     if a in 'aeiouAEIOU':
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('not character')
    

# #32.Wap to find the greatest of 4 numbers. 
# a=int(input('enter the user name: '))
# b=int(input('enter the user name: '))
# c=int(input('enter the user name: '))
# d=int(input('enter the user name: '))
# if a >= b and a >= c and a >= d:
#     print(a)
# elif b >= a and b >= c and b >= d:
#     print(b)
# elif c >= a and c >= b and c >= d:
#     print(c)
# else:
#     print(d)


# # 33. Wap to print the value as it is only if the length of the value is even. 
# a=(input('enter the user name: '))
# if len(a)%2==0:
#     print(a)
# else:
#     print('not even',a)


# # 34.Wap to print the last value of a list only if it is palindrome string starting with vowel. 
# a=[10, 20, "omjomo"]
# if type(a[-1])==str:
#     if a[-1]==a[-1][::-1]:
#         if a[-1][0] in 'aeiouAEIOU':
#             print(a[-1])
#         else:
#             print('not vowel')
#     else:
#         print('not palandrom')
# else:
#     print('not string')


# # 35.Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value. 
# a='apple'
# if len(a)%2==1:
#     if a[0] in 'aeiouAEIOU':
#         if a[-1] not in 'aeiouAEIOU':
#             print(a[::-1])
#         else:
#             print('not consonant')
#     else:
#         print('not vowel')
# else:
#     print('not middle value')


# # 36.Wap to find the second greatest of 4 values. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a >= b and a >= c and a >= d:
#     second = max(b, c, d)
# elif b >= a and b >= c and b >= d:
#     second = max(a, c, d)
# elif c >= a and c >= b and c >= d:
#     second = max(a, b, d)
# else:
#     second = max(a, b, c)
# print("Second greatest =", second)


# # 37.Wap to find the smallest of 4 numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a<=b and a<=c and a<=d:
#     print(a) 
# elif b<=a and b<=c and b<=d:
#     print(b) 
# elif c<=a and c<=b and c<=d:
#     print(c)
# else:
#     print(d)


# # 38. Write a program to print middle Character of the given string only if it is upper Case Character. 
# a='aLe'
# midd=len(a)//2
# if len(a)%2==1:
#     if 'A'<=a[midd]<='Z':
#         print(a[midd]) 
#     else:
#         print('lower case')
# else:
#     print('not midd valu')


# ------------------------------------------------------------------------------------------------------------------------

# # While loop practice :

# # 39.Wap to print python for 5 times. 
# i=1
# while i<=5:
#     print('python')
#     i=i+1


# # 40.Wap to print n natural numbers. 
# a=int(input('enter the value: '))
# i=1
# while a>=i:
#     print(i)
#     i=i+1


# # 41.Wap to print multiplication table for n. 
# a=int(input('enter the value: '))
# i=1
# while i<=10:
#     print(a*i)
#     i=i+1


# # 42.Wap to find the sum of n natural numbers. 
# n = int(input("Enter n: "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("Sum =", sum)


# # 43. Wap to find the product of n natural numbers or factorial of a number. 
# n = int(input("Enter n: "))
# i = 1
# fact = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print("Factorial =", fact)


# # 44.Wap to print all the characters of a string. 
# a='Prajwal'
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1


# # 45.Wap to print all the characters present at even index of a string. 
# a='Prajwal'
# i=0
# while i<len(a):
#     if i%2==0:
#         print(a[i])
#     i=i+1


# # 46.Wap to extract all the lowercase characters present in a string. 
# a='PraJwAl'
# i=0
# while i<len(a):
#     if 'a'<=a[i]<='z' :
#         print(a[i])
#     i=i+1


# # 47.Wap to extract all the vowels present in a string. 
# a='prajwal'
# i=0
# while i<len(a):
#     if a[i] in 'aeiouAEIOU':
#         print(a[i])
#     i=i+1


# # 48.Wap to print factors of a integer number. 
# n = int(input("Enter n: "))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i=i+1


# # 49.Wap to toggle a string. 
# a='PraJwAl'
# i=0
# result=''
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         result=result+(chr(ord(a[i])+32))
#     elif 'a'<=a[i]<='z':
#         result=result+(chr(ord(a[i])-32))
#     i=i+1
# print(result)


# # 50.Wap to reverse the given number. 
# n = 2569
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print("Reverse =", rev)


# # 51.Wap to find the sum of individual digits of a number. 
# a=12345
# i=0
# add=0
# while i<a:
#     digit=a % 10
#     add=add + digit
#     a=a//10
# print(add)


# # 52. Wap to check whether the number is perfect or not. 
# n = int(input("Enter number: "))
# i = 1
# sum = 0
# while i < n:
#     if n % i == 0:
#         sum = sum + i
#     i = i + 1
# if sum == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")


# # 53.Wap to login to phonepe by entering correct otp. 
# correct_otp = 1234
# while True:
#     otp = int(input("Enter OTP: "))
#     if otp == correct_otp:
#         print("Login Successful")
#         break
#     else:
#         print("Invalid OTP")


# # 54.Wap to run infinite loop until user enters the correct password. 
# correct_password = "python123"
# while True:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         print("Wrong Password")


# # 55.Wap to extaract all the even integers present in a tuple at odd index. 
# a=(1,2,3,4,5,6,7,8)
# i=0
# while i<len(a):
#     if i%2!=0:
#         if a[i]%2==0:
#             print(a[i])
#     i=i+1


# # 56.Wap to remove duplicates from a list without converting into set. 
# a=[1,2,3,1,5,3]
# i=0
# result=[]
# while i < len(a):
#     if a[i] not in result:
#         result.append(a[i])
#     i=i+1
# print(result)


# # 57.Wap to find the sum of all the odd numbers between the given range. 
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# i = start
# sum = 0
# while i <= end:
#     if i % 2 != 0:
#         sum = sum + i
#     i = i + 1
# print("Sum =", sum)


# # 58.Wap to find the greatest number in a given list of integers. 
# a = [10, 45, 23, 78, 12]
# i = 1
# greatest = a[0]
# while i < len(a):
#     if a[i] > greatest:
#         greatest = a[i]
#     i = i + 1
# print("Greatest =", greatest)


# # 59.Wap to find the sum of cube of a number in a string. 
# a = input("Enter string: ")
# i = 0
# sum = 0
# while i < len(a):
#     if '0' <= a[i] <= '9':
#         sum = sum + int(a[i]) ** 3
#     i = i + 1
# print("Sum =", sum)


# # 60.Wap to check whether the number is Armstrong or not. 
# a = 153
# b = a
# total = 0
# cube = 0
# while a > 0:
#     t = a % 10
#     cube = t ** 3
#     total = total + cube
#     a = a // 10
# if total == b:
#     print("Armstrong")
# else:
#     print("Not Armstrong")