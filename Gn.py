# 猜數字遊戲
#•	隨機產生一個 1 到 100 的整數答案。
#•	玩家每次輸入猜測數字，程式提示「大了」或「小了」。
#•	答對時顯示「恭喜通過！」並結束遊戲。
#•	程式需記錄猜測次數，顯示學員的持續進步。
import random
def guess_number_game():
    answer = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！請猜一個 1 到 100 的整數。")

    while True:
        try:
            guess = int(input("請輸入你的猜測："))
            attempts += 1

            if guess < 1 or guess > 100:
                print("請輸入介於 1 到 100 之間的數字。")
                continue

            if guess < answer:
                print("小了！再試一次。")
            elif guess > answer:
                print("大了！再試一次。")
            else:
                print(f"恭喜通過！你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的整數。")
if __name__ == "__main__":
    guess_number_game()