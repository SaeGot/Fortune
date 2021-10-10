import random


class FortuneCookie:
    def __init__(self, fortune_List):
        self.__fortuneList = fortune_List
        self.__fortuneCookies = []
        self.__MakeFortuneCookies()


    def SelectFortune(self):
        '''
        점괘 뽑기

        :return:    점괘결과
        '''
        print("포춘쿠키 점괘 뽑기 시작")
        number_of_cookies = len(self.__fortuneCookies)
        random_number = random.randrange(0, number_of_cookies)
        print("쿠키 내용 =", self.__fortuneCookies)
        print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
        fortune_result = self.__fortuneCookies.pop(random_number)
        print("뽑힌 점괘 = " + fortune_result + "\n")
        return fortune_result


    def __MakeFortuneCookies(self):
        '''
        점괘 포춘쿠키에 넣기

        :return:    포춘쿠키 리스트
        '''
        # 점괘 쿠키에 집어넣기
        for fortune in self.__fortuneList:
            cookie_count = fortune[1]
            for n in range(cookie_count):
                self.__fortuneCookies.append(fortune[0])

        print("포춘 쿠키 완성, 쿠키내용 =", self.__fortuneCookies, "\n")




