import random

answer = random.randint(100, 999)

print("=== 3桁の数字当てゲーム ===")

while True:

    guess = int(input("数字を入力してください："))

    if guess == answer:
        print("正解！")
    else:
        print("不正解")

        if guess < answer:
            print("それより大きい数字です")

        else:
            print("それより小さい数字です")

        difference = abs(answer - guess)

        if difference <= 10:
            print("かなり近いです")

        elif difference <= 50:
            print("近いです")

        else:
            print("まだ遠いです")