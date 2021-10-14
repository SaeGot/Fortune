from Fortune import Fortune
import random
from typing import Tuple


class FortuneCookie(Fortune):
    def __init__(self, fortune_Results: list, pity_System: Tuple[int, str]):
        super().__init__(fortune_Results, pity_System)


    def SelectFortune(self) -> int:
        '''
        점괘 뽑기

        :return:    점괘결과
        '''
        print("점괘 뽑기 시작")
        if self._pity_Count >= self._pity_Number:
            print("천장 시스템 발동")
            self._pity_Count = 0
            print("뽑힌 점괘 = " + self._pity_Fortune + "\n")
            return self._pity_Fortune

        number_of_cookies = len(self._fortuneList)
        random_number = random.randrange(0, number_of_cookies)
        print("쿠키 내용 =", self._fortuneList)
        print("전체 쿠키 개수 = " + str(number_of_cookies) + ", 랜덤 숫자 = " + str(random_number))
        fortune_result = self._fortuneList.pop(random_number)

        if fortune_result == self._pity_Fortune:
            self._pity_Count = 0
            print("천장 뽑기 횟수 초기화")
        else:
            self._pity_Count += 1
        print("뽑힌 점괘 = " + fortune_result + "\n")
        return fortune_result