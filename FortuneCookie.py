from Fortune import Fortune
import random
from typing import Tuple


class FortuneCookie(Fortune):
    def __init__(self, fortune_Results: list, pity_System: Tuple[int, str]):
        """
        포춘쿠키형 점괘

        :param fortune_Results:     점괘결과
        :param pity_System:         [천장 도달까지의 필요 뽑기 횟수(0이면 천장 없음), 천장 점괘]
        """
        super().__init__(fortune_Results, pity_System)


    def SelectFortune(self) -> int:
        """
        점괘 뽑기

        :return:    점괘결과
        """
        print("점괘 뽑기 시작")
        if self._pityCount >= self._pityNumber:
            print("천장 시스템 발동")
            self._pityCount = 0
            print("뽑힌 점괘 = " + self._pityFortune + "\n")
            return self._pityFortune

        number_of_cookies = len(self._fortuneList)
        random_number = random.randrange(0, number_of_cookies)
        print("쿠키 내용 =", self._fortuneList)
        print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
        fortune_result = self._fortuneList.pop(random_number)

        if fortune_result == self._pityFortune:
            self._pityCount = 0
            print("천장 뽑기 횟수 초기화")
        else:
            self._pityCount += 1
        print("뽑힌 점괘 = " + fortune_result + "\n")
        return fortune_result