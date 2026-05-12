numXs = int(input('How many times should I print the letter X?'))
toPrint = ''
num = abs(numXs)
while(num != 0):
    toPrint = toPrint + 'X'
    num -= 1
print(toPrint)
