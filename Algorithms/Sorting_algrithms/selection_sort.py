lst=[]
length=int(input("Enter the length of list:"))
print("Enter the element of the list:")
for i in range (length):
    x=int(input())
    lst.append(x)

for i in range (length):
    min_index=i
    for j in range(i+1,length):
        if(lst[j]<lst[min_index]):
            min_index=j

    lst[i],lst[min_index]=lst[min_index],lst[i]

print(lst)