#print("Hello World!")

#single line comments 

"""multi
line
comment"""

#variable is a container which stores the data
"""var1= "hello world"
var2 = 4
var3 = 36.8
var4 = " Hellloooo"
print(type(var1))
print(var1 + var4)

#string to integer conversion
var1 = " 54"
var2 = "32"
print(int(var1)+ int (var2))
print(10* "Hello World\n")
print(100* str(int(var1) + int(var2)))

#input kese lete h
print("Enter a number : ")
number = input()
print("You entered" ,int(number)  + 10)

#add two numbers
print("Enter 1st number: " )
num1 = input()
print("Enter 2nd number: ")
num2 = input()
print("Sum is ",int(num1) + int(num2))

#Dictionary
D = { " pandemic" : "mahamari" , "lynched" : " to kill" , "hailstones" : "olee" , "resentment" : "narazgi" }
print("enter the word: " )
words = str(input())
print(D[words])


#Age Greater than 18 or not
print("Enter the age: ")
age = int(input())
if age > 18:
    print("Eligible to Drive")
elif age == 18:
    print(" Can't decide !!!")
else:
    print("Not Eligible") 


#Faulty Calculator  
print("Enter the first value: ")
a = int(input())   
print("Enter the second value: ") 
b = int(input())
print("Enter the operator: ")
op = input()
if a == 45 and b == 3 and op == '*':
    print(555)
elif a == 56 and b == 9 and op == '+':
    print(77)
elif a == 56 and b == 6 and op == '/' :
    print(4)    
else:
    if op == '+':
        print("sum is", int(a)  + int(b))
    elif op == '-':
        print("sub is", int(a) - int(b))
    elif op == '*':    
        print("mul is", int(a) * int(b))
    else:
        print("div is", int(a) / int(b))


#list that contains everything
list1 = [ 1 , "aastha " , int , 4 , 6 , 9 , 10 , " priyank" ," projo" , float ]
for item in list1:
    if  str(item).isnumeric() and item > 6:
        print(item)


#check till the number becomes greater than 100
print("Enter the number:")
num = int(input())
if num > 100:
    print ("congratulations")
else:
    print("try again")"""



"""total no of guess 9
take the input
reduce the chances left 

tot_guess = 9 
def no_of_guesses(guess):
    print("Enter the time you are guessing:")
    guess=int(input())
    if guess==1:
        print("Number of guesses left:",tot_guess-1)
    elif guess==2:
        print("Number of guesses left:",tot_guess-2)
    elif guess==3:
        print("Number of guesses left:",tot_guess-3)
    elif guess==4:
        print("Number of guesses left:",tot_guess-4)
    elif guess==5:
        print("Number of guesses left:",tot_guess-5)
    elif guess==6:
        print("Number of guesses left:",tot_guess-6)
    elif guess==7:
        print("Number of guesses left:",tot_guess-7)
    elif guess==8:
        print("Number of guesses left:",tot_guess-8)
    else:
        print("No more chances left!!!") 
    
   

def Guess_the_number(num):
    print("Enter the number:")
    num = int(input()) 
    if(num > 18):
            print("Wrong Answer!! Too high")
    elif (num < 18):
            print("Wrong Answer!! Too low")
    else:
        print("Correct Answer!! Good luck...")


chosen_number = Guess_the_number(18)
no_of_chances = no_of_guesses(9)

chosen_number = Guess_the_number(18)
no_of_chances = no_of_guesses(9)

chosen_number = Guess_the_number(18)
no_of_chances = no_of_guesses(9)

chosen_number = Guess_the_number(18)
no_of_chances = no_of_guesses(9)

Another APPROACH
def Guess_the_number():
    guess= 18
    for i in range(1,10):
        num = int(input("Enter Guess Number: ")) 
        if(num == guess):
            print("Correct Answer!! Good luck... ",guess)
            break
        elif (num < guess):
            print("Wrong Answer Too Low")
        elif (num > guess):
            print("Wrong Answer!! Too  high")
        if(i==9):
            print("No More Guess Left")
            break
        else:
            print(f"No. of Guesses Left = {9-i}")

Guess_the_number()  

"""

