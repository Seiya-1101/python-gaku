# 1つの正の整数をユーザに入力させた上、２つの整数root、pwrを表示する
# ただし、1 < pwr < 6、root**pwrは入力した整数値と等しい
x = int(input('Enter an integer: '))
root = 0
pwr = 2
cnt = 0
while(pwr < 6):
    while(root ** pwr < abs(x)):
        root = root + 1
    if(root ** pwr == abs(x)):
        cnt = cnt + 1
        break
    pwr = pwr + 1
    root = 0
if(cnt == 0):
    print('1<pwr<6の範囲でroot**pwr=' + str(x) + 'を満たすペアは存在しないよ')
else:
    print('入力された整数' + str(x) + 'は' + str(root) + 'の' + str(pwr) + '乗だよ')
