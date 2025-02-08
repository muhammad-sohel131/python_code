from itertools import count

list1 = ["apple","banana","cherry"]
print(list1)

list2 = ['abc',34, True]
print(list2)

# list constructor
thisList = list(('apple','banana','cherry', 'orange','kiwi','melon','mango'))
print(thisList)
print(thisList[-1])
print(thisList[-7:-6])  #[low,high]

thisList.append("Orange")
print(thisList)
thisList[4]="mango"
print(thisList)

thisList.insert(1,"kiwi")
print(thisList)

thisList.remove("mango")
print(thisList)

thisList.pop(2)
print(thisList)

for x in thisList:
    print(x)

print(len(thisList))

for i in range(len(thisList)):
    print(thisList[i])
thisList.sort()
print(thisList)
myList = thisList.copy()

thisList = [100,50,65,82,23]
thisList.sort()
print(thisList)

newList = myList + thisList
print(newList)
myList.extend(thisList)
print(myList)
thisList.clear()
print(thisList)

print(myList.count('orange'))
newList += list1
print(newList)