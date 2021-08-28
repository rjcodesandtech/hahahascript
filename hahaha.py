import sys
codeString = ""  
codeFile = sys.argv[1]
f = open(codeFile, "r")
fileString = f.read()
f.close()
if '\n' in fileString:
    fileString = fileString.replace('\n','')
fileString = fileString.replace('H', '1')
fileString = fileString.replace('A', '0')
j = 0
def split(word):
    return [char for char in word]
listChar = split(fileString)
processedList = listChar
for i in range(len(listChar)):
    if i % 8 == 7:
        j = j + 1
        processedList.insert(i+j, ' ')
processedString = ''.join(processedList)
binary_values = processedString.split()
for binary_value in binary_values:
    an_integer = int(binary_value, 2)
    ascii_character = chr(an_integer)
    codeString += ascii_character
del j, listChar, binary_values, processedList, processedString, fileString
exec(codeString)