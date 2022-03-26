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

"""def getSum(arr,n):
    min = getMin(arr,n)
    max = getMax(arr,n)
    sum = min+max
    return sum"""

if __name__ == '__main__':
    arr = [9,2,6,4,1]
    n = len(arr)

    min = getMin(arr,n)
    max = getMax(arr,n)
    #ans = getSum(arr,n)
    
    print("minimum value is: " , min)
    print("maximum value is: " , max)
    #print("sum of min and max is: ", ans )