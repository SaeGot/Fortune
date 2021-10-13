import random


class Fortune:
    def __init__(self, fortune_Results: list):
        '''
        
        :param fortune_Results:    점괘결과
        '''
        self._fortuneResults = fortune_Results
        self._fortuneList = []
        self._MakeFortuneList()


    def SelectFortune(self) -> int:
        '''
        점괘 뽑기

        :return:    점괘결과
        '''
        print("점괘 뽑기 시작")
        number_of_cookies = len(self._fortuneList)
        random_number = random.randrange(0, number_of_cookies)
        print("쿠키 내용 =", self._fortuneList)
        print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
        fortune_result = self._fortuneList[random_number]
        print("뽑힌 점괘 = " + fortune_result + "\n")
        return fortune_result


    def _MakeFortuneList(self):
        '''
        점괘결과 점괘 리스트에 넣기
        '''
        # 점괘결과 점괘 리스트에 넣기
        for fortune in self._fortuneResults:
            cookie_count = fortune[1]
            for n in range(cookie_count):
                self._fortuneList.append(fortune[0])

        print("점괘 리스트 완성 : ", self._fortuneList, "\n")