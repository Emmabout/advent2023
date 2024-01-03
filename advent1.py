
import re

f = open('advent1_input.txt', 'r')
content = f.read().splitlines()
print(content)

digitsLetters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = [1,2,3,4,5,6,7,8,9]

test = content[:5]
print(test)
sum = 0

for word in content:
    listOfNumbers = []
    listOfIndexes = []
    for i, digit in enumerate(digitsLetters):
        occurences = [m.start() for m in re.finditer(digit, word)]
        for oc in occurences:
            listOfNumbers.append(i+1)
            listOfIndexes.append(oc)
    
    for i, digit in enumerate(digits):
        occurences = [m.start() for m in re.finditer(str(digit), word)]
        for oc in occurences:
            listOfNumbers.append(i+1)
            listOfIndexes.append(oc)
    #print(listOfNumbers)
    #print(listOfIndexes)
    firstNumber = listOfNumbers[listOfIndexes.index(min(listOfIndexes))]
    lastNumber = listOfNumbers[listOfIndexes.index(max(listOfIndexes))]
    #print(firstNumber, lastNumber)
    #print(int(str(listOfNumbers[0]) + str(listOfNumbers[-1])))
    sum += int(str(firstNumber) + str(lastNumber))

print(sum)
