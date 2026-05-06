# 複合論理式を使った条件の評価
x = 3
y = 6
z = 99

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')
    