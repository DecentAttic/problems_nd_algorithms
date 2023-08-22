# Bubble sort:

# 1.Comparing and Swapping: Bubble Sort starts at the beginning of the list and compares adjacent pairs of elements. 
# If the elements are in the wrong order (i.e., the current element is greater than the next element), it swaps them.
# One Pass Through the List: The algorithm makes one complete pass through the list, comparing and swapping elements as necessary.

# 2.Multiple Passes: Bubble Sort repeats this process multiple times (n-1 passes for a list of n elements) until no more swaps are required in a pass.
# If no swaps are made during a pass, the list is considered sorted, and the algorithm terminates early.

# 3.Complexity: The time complexity of Bubble Sort is O(n^2) in the worst and average cases, where n is the number of elements in the list. In the best case,
# where the list is already sorted, it has a time complexity of O(n).



def swap(a,b):
    t=a
    a=b
    b=t
    return a,b

lst=[]

length=int(input("Enter the length of list: "))
print("Enter the elements:")
for i in range(length):
    x=int(input())
    lst.append(x)
print("Array before sorting:",lst)
for i in range(length-1):
    for j in range(0,length-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=swap(lst[j],lst[j+1])

print("Array after sorting",lst)