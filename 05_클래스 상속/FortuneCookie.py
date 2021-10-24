from Fortune import Fortune
import random


class FortuneCookie(Fortune):
    def __init__(self, fortune_Results: list):
        super().__init__(fortune_Results)

    def SelectFortune(self) -> int:
        """
        포춘쿠키형 점괘

        :return:    점괘결과
        """
        print("점괘 뽑기 시작")
        number_of_cookies = len(self._fortuneList)
        random_number = random.randrange(0, number_of_cookies)
        print("쿠키 내용 =", self._fortuneList)
        print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
        fortune_result = self._fortuneList.pop(random_number)
        print("뽑힌 점괘 = " + fortune_result + "\n")
        return fortune_result
