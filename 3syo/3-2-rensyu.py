total = 0
x = '1.23, 2.4, 3.123' # 少数を含む文字列
for c in x.split(","):
    total = total + float(c)
print(total)
