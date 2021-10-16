from FortuneCookie import FortuneCookie
from Fortune import Fortune
from CSVReader import CSVReader

if __name__ == '__main__':
    data_type = ["str", "int"]
    csv_read = CSVReader("FortuneList.csv", data_type)
    fortune_list = csv_read.GetData()

    fortune_cookie = FortuneCookie(fortune_list, (2, "좋음"))
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()