name = input('Enter your name: ')
print('Are you really', name, '?') # printは複数の引数を与えられると間に空白を置く
print('Are you really ' + name + '?') # 空白を含まない文字列を作るために連結を用いている

n = input('Enter an int:')
print(type(n)) # 入力された値は整数型ではなく文字列
print(n * 4)
print(int(n) * 4) # 型変換を用いて整数型として計算している

print(int(3.9))# 浮動小数点数を整数に変換すると切り捨て
# -*- coding: encoding name -*-
# どのエンコードを使うかPythonに伝えることだできる

# -*- coding: utf-8 -*-  # PythonにUTF-8を使うように指示をする
# ほとんどのPythonの実装ではデフォルトでUTF-8になっている
