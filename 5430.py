from collections import*
N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr=sorted(arr)
print(round(sum(arr)/N))
print(arr[N//2])
if len(arr)>=2:
    if Counter(arr).most_common()[0][1] == Counter(arr).most_common()[1][1]:
        print(Counter(arr).most_common()[1][0])

    else:
        print(Counter(arr).most_common()[0][0])
else:
    print(arr[0])
print(arr[-1]-arr[0])
