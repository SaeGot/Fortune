import random

def SelectFortune(fortune_list):
    '''
    :param fortune_list:    점괘결과 목록
    :return:        점괘결과
    '''

    fortune_cookie = []

    #점괘 쿠키에 집어넣기
    for fortune in fortune_list:
        cookie_count = fortune[1]
        for n in range(cookie_count):
            fortune_cookie.append(fortune[0])

    number_of_cookies = len(fortune_cookie)
    random_number = random.randrange(0, number_of_cookies)
    fortune_result = fortune_cookie[random_number]
    print("쿠키 내용 =", fortune_cookie)
    print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
    return fortune_result


if __name__ == '__main__':
    fortune_list = [["좋음", 3], ["보통", 2], ["나쁨", 1]]
    print(SelectFortune(fortune_list))