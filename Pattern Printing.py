
def Print_pattern(n):
    for i in range(0,n):#no of rows
        for j in range(0,i+1):#no of columns
            print("*" ,end=" ")
        print("\r")#newline
n=5
Print_pattern(n)  
   








def Pattern_True(n):
    #n1 = bool(input("t/f"))
    #if n1==True:
        for i in range(0,n):
            for j in range(0,i+1):
                print("*" , end="")
            print("\r")
    #if n1==False:

def Pattern_False(n):   
        for i in range(1,n):
            for j in range(0,n):
                
                print("*",end="")
            print("\r")
        for i in range(2,n):
            for j in range(2,i-1):
                print(" ")

n = 6
print("For true:")
Pattern_True(n) 
print("For false:")
Pattern_False(n)                 


