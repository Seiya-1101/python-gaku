# forループ
# for 変数 in シーケンス:
#   コードブロック
#  シーケンスは、通常、組み込み関数であるrangeを用いて作られる
r1 = range(5, 40, 10) # (開始(start), 終了(stop), ステップ(step))  シーケンス5,15,25,35を生成する
r2 = range(40, 5, -10) # シーケンス40,30,20,10を生成する
r3 = range(0,3) # 最初の引数を省略した場合デフォルトは0  　シーケンス0,1,2を生成する
r4 = range(3) # 最後の要素(ステップ)を省略した場合は、デフォルトは1    ↑と同じくシーケンス0,1,2を生成する

x = 4
for i in range(0, x):
    # print(i)
    x = 5  
    # for分がある行のrange関数の引数は最初の繰り返しの際だけ評価され、それ以降は再評価されない

x = 4
for j in range(x):
    for i in range(x):
        # print(i)
        x = 2


# 完全立方に対する立方根を求める
x = int(input('Enter an integer: '))
for ans in range(0, abs(x) + 1):
    if ans ** 3 >= abs(x):
        break
if ans ** 3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is ', ans)
