def search(arr,n,key):
    for i in range(0,n):
        if (arr[i] == key):
            return i
    return -1

arr = [2, 3, 4, 10, 40]
key = int(input("enter the value:",))
n = len(arr)

found = search(arr,n,key)
if(found == -1):
    print("key is absent")
else:
    print("key is present")
