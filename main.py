import random

answer = random.randint(100, 999)

print("=== 3桁の数字当てゲーム ===")

max_attempts = 7
count = 0

while count < max_attempts:

    try:
        guess = int(input("数字を入力してください："))
    except ValueError:
        continue

    count += 1

    if guess == answer:
        print("正解！")
        print(f"{count}回で成功")
        break

    else:
        print("不正解")

        if guess < answer:
            print("ヒント：それより大きい数字です")

        else:
            print("ヒント：それより小さい数字です")

        difference = abs(answer - guess)

        if difference <= 10:
            print("ヒント：かなり近いです")

        elif difference <= 50:
            print("ヒント：近いです")

        else:
            print("ヒント：まだ遠いです")

        print(f"残り{max_attempts - count}回")

else:
    print("ゲームオーバー")
    print(f"正解は{answer}でした")