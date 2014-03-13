number = str(input('Number: '))
width = int(input('Width: '))

digit_def = {
        0: (1, 1, 1, 0, 1, 1, 1),
        1: (0, 0, 1, 0, 0, 1, 0),
        2: (1, 0, 1, 1, 1, 0, 1),
        3: (1, 0, 1, 1, 0, 1, 1),
        4: (0, 1, 1, 1, 0, 1, 0),
        5: (1, 1, 0, 1, 0, 1, 1),
        6: (1, 1, 0, 1, 1, 1, 1),
        7: (1, 0, 1, 0, 0, 1, 0),
        8: (1, 1, 1, 1, 1, 1, 1),
        9: (1, 1, 1, 1, 0, 1, 1)}
        
printArr = []
lol = (2*width + 3)
for x in range(lol):
    printArr.append([])
x = 0
backx = x
for i in [0,1,3,4,6]:
    backx = x
    for num in number:
        toPrint = ''
        if i in [0,3,6]:
            if digit_def[int(num)][i] == 1:
                toPrint += ' ' + '-'*width + ' '
            else:
                toPrint += ' '*width + '  '
            printArr[x] += toPrint + ' '
        else:
            x = backx
            for times in range(width):
                toPrint = ''
                if digit_def[int(num)][i] == 1 and digit_def[int(num)][i+1] == 1:
                    toPrint += '|' + ' '*width + '|'
                elif digit_def[int(num)][i] == 1 and digit_def[int(num)][i+1] == 0:
                    toPrint += '|' + ' '*width + ' '
                elif digit_def[int(num)][i] == 0 and digit_def[int(num)][i+1] == 1:
                    toPrint += ' ' + ' '*width + '|'
                else:
                    toPrint += ' ' + ' '*width + ' '
                if width > 1 and times < width and times != 0:
                    x+=1
                printArr[x] += toPrint + ' '
    x += 1
for i in printArr:
    i[-1] = ''
    print(''.join(i))