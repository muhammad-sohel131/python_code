thisTuple = ("cse", "eee", 'bba')
print(thisTuple)

print(thisTuple.count("ee"))

tempList = list(thisTuple)
tempList.append("textile")
thisTuple = tuple(tempList)
print(thisTuple)

print(thisTuple[2])

thisTuple = ('apple', 'banana', 'cherry')
y = ("orange",)
thisTuple += y
print(thisTuple)

newTuple = thisTuple + y
print(newTuple)

(f1,f2,f3,f4) = thisTuple
print(f3)

i = 0
while i < len(newTuple):
    print(newTuple[i])
    i = i + 1