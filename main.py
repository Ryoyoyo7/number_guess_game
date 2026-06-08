import random

answer = random.randint(100, 999)

print("=== 3桁の数字当てゲーム ===")

guess = int(input("数字を入力してください："))

if guess == answer:
    print("正解！")
else:
    print("不正解")