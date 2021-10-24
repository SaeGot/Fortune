import random


def SelectFortune(fortune_List):
    """
    :param fortune_List:    점괘결과 목록
    :return:        점괘결과
    """

    fortune_list_count = len(fortune_List)
    random_number = random.randrange(0, fortune_list_count)
    fortune_result = fortune_List[random_number]
    print("전체 항목 개수 = " + str(fortune_list_count) + ", 랜덤 숫자 = " + str(random_number))
    return fortune_result


if __name__ == '__main__':
    fortune_list = ["좋음", "보통", "나쁨"]
    print(SelectFortune(fortune_list))
