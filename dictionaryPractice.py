thisDict = {
    "brand" : "Ford",
    'model' : 'Mustang',
    'year': 1964
}
print(thisDict)
print(thisDict['model'])
thisDict['year'] = 2018
print(thisDict)
thisDict['month'] = "April"
print(thisDict)

thisDict.pop('year')
thisDict.popitem()
print(thisDict)

for i in thisDict:
    print(thisDict[i])

mydict = thisDict.copy()
thisDict['year'] = 2018
print(mydict)

myFamily = {
    "child1": {
        "name" : "Emil",
        "year" : 2002
    },
    "child2": {
        "name": "Tobias",
        "year" : 2007
    }
}
print(myFamily['child1']['name'])