from FortuneCookie import FortuneCookie
from Fortune import Fortune
from CSVReader import CSVReader

if __name__ == '__main__':
    data_type = ["str", "int"]
    csv_read = CSVReader("FortuneList.csv", data_type)
    csv_read_2 = CSVReader("FortuneList_2.csv", data_type)
    fortune_list = csv_read.GetData()
    fortune_list_2 = csv_read_2.GetData()

    fortune_cookie = FortuneCookie(fortune_list, (2, "좋음"), "1번 박스")
    fortune_cookie_2 = FortuneCookie(fortune_list_2, box_Name="2번 박스")
    fortune_cookie.SelectFortune()
    fortune_cookie_2.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie_2.SelectFortune()