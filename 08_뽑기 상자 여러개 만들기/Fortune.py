import random
from typing import Tuple


class Fortune:
    def __init__(self, fortune_Results: list, pity_System: Tuple[int, str] = (0, ""), box_Name: str = ""):
        """
        일반 점괘

        :param fortune_Results:     점괘결과
        :param pity_System:         [천장 도달까지의 필요 뽑기 횟수(0이면 천장 없음), 천장 점괘]
        :param box_Name:            점괘 박스 이름
        """
        self._fortuneResults = fortune_Results
        self._pityNumber = pity_System[0]
        self._pityFortune = pity_System[1]
        self._pityCount = 0
        self._boxName = box_Name
        self._fortuneList = []

        self._MakeFortuneList()

    def SelectFortune(self) -> str:
        """
        점괘 뽑기

        :return:    점괘결과
        """
        print(self._boxName, "점괘 뽑기 시작")
        if self._pityCount >= self._pityNumber != 0:
            print("천장 시스템 발동")
            self._pityCount = 0
            print("뽑힌 점괘 = " + self._pityFortune + "\n")
            return self._pityFortune

        number_of_cookies = len(self._fortuneList)
        random_number = random.randrange(0, number_of_cookies)
        print("점괘 내용 =", self._fortuneList)
        print("랜덤 숫자 = " + str(random_number))
        fortune_result = self._fortuneList[random_number]

        if fortune_result == self._pityFortune:
            self._pityCount = 0
            print("천장 뽑기 횟수 초기화")
        else:
            self._pityCount += 1

        print("뽑힌 점괘 = " + fortune_result + "\n")

        return fortune_result

    def _MakeFortuneList(self):
        """
        점괘결과 점괘 리스트에 넣기
        """
        # 점괘결과 점괘 리스트에 넣기
        for fortune in self._fortuneResults:
            cookie_count = fortune[1]
            for n in range(cookie_count):
                self._fortuneList.append(fortune[0])

        print("점괘 리스트 완성 : ", self._fortuneList, "\n")
