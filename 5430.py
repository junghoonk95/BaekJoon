from collections import*
import sys

T=int(input())

def AC():
    Func=list(map(str,input()))
    num=int(input())
    arr=str(input())
    if num<Counter(Func)["D"]:

        return print("error")

    elif num==Counter(Func)["D"]==0:
        return print([])

    arr=arr[1:-1]

    arr=deque(arr.split(","))
    k=0

    for i in range(len(Func)):
        if Func[i]=="D":
            if k%2==0:
                arr.popleft()
            else:
                arr.pop()
        else:
            k = k + 1
    for i in range(len(arr)):
        arr[i]=int(arr[i])

    if k%2==1:
        arr=list(reversed(arr))
    else:
        arr=list(arr)

    arr=str(list(arr)).replace("'","").replace(' ','')

    return print(arr)



for i in range(T):
    AC()





