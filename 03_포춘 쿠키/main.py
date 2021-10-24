import random


def SelectFortune(fortune_Cookies):
    """
    점괘 뽑기

    :param fortune_Cookies: 포춘쿠키 리스트
    :return:                점괘결과
    """
    print("포춘쿠키 점괘 뽑기 시작")
    number_of_cookies = len(fortune_Cookies)
    random_number = random.randrange(0, number_of_cookies)
    print("쿠키 내용 =", fortune_Cookies)
    print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
    fortune_result = fortune_Cookies.pop(random_number)
    print("뽑힌 점괘 = " + fortune_result + "\n")
    return fortune_result


def MakeFortuneCookies(fortune_List):
    """
    점괘 포춘쿠키에 넣기

    :param fortune_List:    점괘결과 목록
    :return:                포춘쿠키 리스트
    """
    fortune_cookies = []
    #점괘 쿠키에 집어넣기
    for fortune in fortune_List:
        cookie_count = fortune[1]
        for n in range(cookie_count):
            fortune_cookies.append(fortune[0])

    print("포춘 쿠키 완성, 쿠키내용 =", fortune_cookies, "\n")
    return fortune_cookies


if __name__ == '__main__':
    fortune_list = [["좋음", 3], ["보통", 2], ["나쁨", 1]]

    fortune_cookies = MakeFortuneCookies(fortune_list)
    SelectFortune(fortune_cookies)
    SelectFortune(fortune_cookies)
    SelectFortune(fortune_cookies)
