print(3 * 'a')
print('a' + 'a')

# print(a)　定義されていない
# print('a' * 'a')　文字かける文字はできない
# ↑はエラー

# '2' < 3
# python2だとFalse
# python3だとエラー

print(len('abc'))

print('abc'[0])
print('abc'[2])
print('abc'[-1]) # 負の数は文字列の最後から検索する際に利用できる

# 任意の長さの部分文字列を取り出す　スライス表記
print('abc'[1:3])
print('abc'[0:len('abc')])
print('abc'[:])
