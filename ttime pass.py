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

# 10. Wap to check whether the given integer is multiple of 3. 
a=int(input('enter the value: '))
if a%3==0:
    print("Multiple of 3")