# ユーザに10個の正の整数の入力を促したうえ、その中で最も大きな奇数の値を表示する
max = 0
cnt = 0
x = 0
print('10個の正の整数を入力してください')
while(x < 10):
    temp = int(input(str(x) + '個目の正の整数の入力'))
    if(temp % 2 != 0):
        cnt += 1
        if(temp > max):
            max = temp
    x += 1
if(cnt > 0):
    print('この中で一番大きな奇数は' + str(max) + 'です')
else:
    print('この中に奇数はありません')

