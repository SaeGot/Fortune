import csv


class CSVReader:
    def __init__(self, file_Name: str, data_Type: list):
        """
        CSV 읽기
        
        :param file_Name:        CSV 파일명
        :param data_Type:   데이터 타입
        """
        self._file = open(file_Name, "r", encoding="utf-8-sig")
        self._dataType = data_Type
        self._data = self._ReadData()

    def GetData(self) -> list:
        """
        데이터 가져오기
        
        :return:    데이터 리스트(2차원)
        """
        return self._data

    def _ReadData(self) -> list:
        """
        파일 읽기

        :return:        데이터 리스트(2차원)
        """
        data = []

        # 데이터 읽기
        lines = csv.reader(self._file)
        for line in lines:
            row = []
            for col_num, value in enumerate(line):
                if self._dataType[col_num] == "int":
                    row.append(int(value))
                else:
                    row.append(value)
            data.append(row)

        return data
