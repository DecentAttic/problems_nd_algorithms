lst=[]
length=int(input("Enter the length of List "))
for i in range(length):
    x=int(input())
    lst.append(x)
key=int(input("Enter the key to be searched "))
flag=0   
for i in range(length):
    if key==lst[i]:
        flag=1
        pos=i
        break
if flag==1:
    print("Element found at pos:",pos+1)
else:
    print("Not found")
        
    