import random

answer = random.randint(100, 999)

print("=== 3桁の数字当てゲーム ===")

guess = int(input("数字を入力してください："))

if guess == answer:
    print("正解！")
else:
    print("不正解")

    if guess < answer:
        print("もっと大きい数字です")

    else:
        print("もっと小さい数字です")