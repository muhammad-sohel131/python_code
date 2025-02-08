list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input())
    list.append(ele)

print(list)
print("Sum of elements in given list is : ", sum(list))

def max_number(lst):
    mx = list[0]
    for a in lst:
        if a > mx:
            mx = a
    return mx
print(max_number(list))