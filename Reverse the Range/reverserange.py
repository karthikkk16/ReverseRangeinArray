'''Given an array A of N integers and also given two integers B and C.
 Reverse the elements of the array A within the given inclusive range [B, C].
 '''
def reverserange(arr,s,e):
    i=s
    j=e
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

a=list(map(int,input().split()))
s=int(input())
e=int(input())
print(reverserange(a))