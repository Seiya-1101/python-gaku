# 3つの正の変数x,y,zを調べ、その中で最も大きい奇数を表示する
x, y, z = 610, 70, 520
max = 0

if (x % 2 == 0):
    if(y % 2 == 0):
        if (z % 2 == 0):
            print('この中に奇数はないよ')
        else:
            max = z
    else:
        if (z % 2 == 0):
            max = y
        elif (y > z):
            max = y
        else:
            max = z
else:
    if (y % 2 ==0):
        if (z % 2 == 0):
            max = x
        elif (x > z):
            max = x
        else:
            max = z
    elif(z % 2 == 0):
        if(x > y):
            max = x
        else:
            max = y
    else:
        if(x > y and x > z):
            max = x
        elif(y > x and y > z):
            max = y
        else:
            max = z

print('この中で一番大きい奇数は', max, 'です')
