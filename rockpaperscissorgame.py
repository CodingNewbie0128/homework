import random

value_list = ["가위","바위","보"]
win = 0
lose = 0
draw = 0


def computer_value():
    num = random.randint(0, 2)
    return value_list[num]


def user_input_value():
    while True:
        user_value = input("가위, 바위 , 보 중 하나를 선택하세요: ")
        if user_value in value_list:
            return user_value
        else:
            print("유효한 입력이 아닙니다")


def user_win():
    global win
    win += 1
    print("이겼습니당")


def computer_win():
    global lose
    lose += 1
    print("졌습니당")


def both_same():
    global draw
    draw += 1
    print("무승부")


def ask_to_play_again():
    while True:
        yesorno = input("다시 하시겠습니까 (y/n) :")

        if yesorno == "y" or yesorno == "Y":
            return True  # 다시 게임을 해야함
        elif yesorno == "N" or yesorno == "n":
            print("게임을 종료합니다 ")
            return False  # 게임을 종료해야함

        else:
            print("y or n 로만 입력하세요")  # y or n 로만 대답해야함


def statistic():
    global draw
    global win
    global lose
    print("승 : {} 패 : {} 무승부 {}".format(win, lose, draw))


def compare(a, b):
    if a == b:
        both_same()
    elif (a == "가위" and b == "보") or (a == "바위" and b == "가위") or (a == "보" and b == "바위"):
        computer_win()
    else:
        user_win()


def game():
    while True:
        computer = computer_value()
        user = user_input_value()
        print("컴퓨터 : {}".format(computer))
        compare(computer, user)

        if not ask_to_play_again():  # y 면 not True 값으로되서 break가 실행이안되고 N 이면 False로되서 break된다
            print("게임을 종료합니다")
            statistic()
            break;


def main():
    game()


if __name__ == "__main__":
    main()
