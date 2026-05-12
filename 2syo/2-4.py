# 繰り返し
# while分
# 整数の２乗を地道に求める
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):  # xが負の値のとき危険(永遠ループ)
    ans = ans + x
    itersLeft = itersLeft - 1
print (str(x) + '*' + str(x) + ' = ' + str(ans))

# 整数の２乗を地道に求める(改良版)
x = -3
ans = 0
itersLeft = abs(x)
while (itersLeft != 0):  # xが負の値のとき危険(永遠ループ)
    ans = ans + abs(x)
    itersLeft = itersLeft - 1
print (str(x) + '*' + str(x) + ' = ' + str(ans))


# 11と12ともに割り切れる正の整数を見つける
x = 1
while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')
