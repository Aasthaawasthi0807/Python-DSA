
# Sum of Min and Max element of array

def getMin(arr,n):
    res = arr[0]
    for i in range(1 , n):
        res = min(res , arr[i])
    return res

def getMax(arr,n):
    res = arr[0]
    for i in range(1 , n):
        res = max(res , arr[i])
    return res

def getSum(arr,n):
    min = getMin(arr,n)
    max = getMax(arr,n)
    
    return min+max

if __name__ == '__main__':
    arr = [99,2,6,4,8]
    n = len(arr)

    #min = getMin(arr,n)
    #max = getMax(arr,n)
    #ans = getSum(arr,n)
    
    #print("minimum value is: " , min)
    #print("maximum value is: " , max)
    print("sum of min and max is: ", getSum(arr,n))



#print sum of all elements in an array

def arrSum(arr,n):
    sum = 0
    for i in range(n):
        sum = arr[i] + sum
        i+=1
    return sum
        

if __name__ == '__main__':
    arr = [9,1,4,6,3,0]
    n = len(arr)

    print("Sum of all the elements in array:" , arrSum(arr,n))