# 平方根を求めるためのニュートン-ラフソン法
# x**2 - 24 = 0 で　誤差がepsilon以下になる x を求める
epsilon = 0.01
k = 24.0
guess = k / 2.0
numGuesses = 0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2)- k)/ (2 * guess))
    numGuesses += 1
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)
