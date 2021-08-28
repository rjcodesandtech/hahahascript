import sys
codeString = ""  
codeFile = sys.argv[1]
f = open(codeFile, "r")
fileString = f.read()
f.close()
def binaryStringToHAHAHA(binCode):
    toA = binCode.replace("0", "A")
    toH = toS.replace("1", "H")
    return toH
res = ''.join(format(ord(i), '08b') for i in fileString.upper())
binaryString = str(res)
genFile = codeFile.replace('.py', '') + ".hahaha"
f = open(genFile, "w")
f.write(binaryStringToHAHAHA(binaryString))
f.close()
print("Code file " + codeFile + " successfully converted to " + genFile)