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

# 27. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, 
# if it is digit print the reminder when  it is divided by 3 else if it is special character print it’s ASCII value. 
a = (input("Enter first number: "))
if 'a'<=a<='z':
    print((chr(ord(a)-32)))
elif 'A'<=a<='Z':
    print(a.lower())
elif '0' <= a <= '9':
    print(int(a) % 3)
else:
    print(ord(a))
    
