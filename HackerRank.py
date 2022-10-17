#Hacker Rank Challenges

#Practice with range with numbers for specific response
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

n = int(input("Enter input: ").strip())

if n % 2 != 0:
    print ("Weird")  # != means not equal to 0 and % means after dividing it gives a remainder 
else:
    if n >= 2 and n <=5:
        print("Not weird")  # 2-5 statement greater than or equal to and  less than equal to used for first elif as well
    elif n >= 6 and n <= 20:
        print("Weird") # 6-20 statement
    elif n > 20:
        print("Not Weird") # greater than 20

#Practice with Arithmetic Operators    
#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
    
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

#Practice Division
#The provided code stub reads two integers,  and , from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#No rounding or formatting is necessary.

a = int(input())
b = int(input())
print(a//b)
print(a/b)

#Practice Loops
#The provided code stub reads and integer, , from STDIN. For all non-negative integers i < ,i^2 print .
n = int(input())
for n in list(range(n)):
    print(n**2)

#Write a function
#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
def is_leap(year): # Def creates functions in Python
    leap = False
    if year%4 == 0:
        leap = True
    if year%4 == 0 and year%100 == 0:
        leap = False
    if year%4 == 0 and year%100 == 0 and year%400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#Print Function
#Example
# n = 5
#Print the string 12345.
n = int(input())
for x in range(1,n+1): # The n+1 creates the last range number so for example 3 will give 4 and so we will start with index 1 and go up to index 4 
    print(x, end ="")