# 整数の立方根があればそれを表示する。完全立方根でなければその旨をメッセージとして表示する

# 完全立方根を求める
x = int(input('Enter an interger: '))
ans = 0
while ans ** 3 < abs(x):
    # print('Value of the decremeniting function abs(x) - ans**3 is', abs(x) - ans ** 3)
    # ans = ans
    ans = ans + 1
if ans ** 3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
