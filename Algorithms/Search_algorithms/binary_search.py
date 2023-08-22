# Binary Search

# Step 1: Determine the middle element of the collection.
# Step 2: Compare the middle element with the target element you're searching for.
# Step 3: If the middle element is equal to the target, the search is successful. 
#         If not, determine whether the target is smaller or larger than the middle element.
# Step 4: If the target is smaller, eliminate the right half of the collection (including the middle element). 
#         If the target is larger, eliminate the left half.
# Step 5: Repeat the process with the remaining half of the collection. 
#         Go back to Step 1 until the target element is found or the search interval becomes empty.


lst=[]
length=int(input("Enter the length of list"))
print("Enter the sorted array ")
for i in range(length):
    x=int(input())
    lst.append(x)


key=int(input("Enter the element to be searched "))
start=0
end=length-1
flag=0

while start<=end:
    mid=start+(end-start)//2
    if key==lst[mid]:
        flag=1
        break
    elif key>lst[mid]:
        start=mid+1
    elif key<lst[mid]:
        end=mid-1

if flag==1:
    print("Element found at ",mid+1)
else:
    print("Element not found")


    

