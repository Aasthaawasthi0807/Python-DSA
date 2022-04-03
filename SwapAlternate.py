from tempfile import tempdir
#Swap Alternate using 2 variables

def printarr(arr , n):
    for i in range(n):
        print(arr[i],end="")

def updateArray(arr , n):
    i =0
    j = n-1
    while(i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        i+=2
        j-=2
    printarr(arr,n)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)

    updateArray(arr,n)


#Swap alternate using 1 variable

def printArray(arr,n):
    for i in range(0,n-1):
        print(arr[i],end="")

def updatearr(arr,n):
    for i in range(0,n-1):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i+=2

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    n = len(arr)

    updatearr(arr,n)
    printArray(arr,n)
