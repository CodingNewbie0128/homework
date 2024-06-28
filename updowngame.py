import random


def setNum():
    num=random.randint(1,100)
    return num
def game():
    count=1
    num=setNum()

    while True:
        user_num = int(input("숫자를 입력하세요 :"))
        if user_num > 100 or user_num < 1:
            print("유효한 범위 내의 숫자를 입력하세요")
            game()
        if num==user_num:
            print("맞았습니다\n시도한 횟수 :{}".format(count))
            decision=input("다시 하겠습니까? (y/n) ")
            if decision=="y":
                game()

            if decision=="n":
                break;
        elif num<user_num:
            print("down")
            count += 1
        else :
            print("up")
            count += 1

    print("게임을 종료합니다")



game()








