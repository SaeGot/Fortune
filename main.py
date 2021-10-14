from FortuneCookie import FortuneCookie
from Fortune import Fortune

if __name__ == '__main__':
    fortune_list = [["좋음", 1], ["보통", 2], ["나쁨", 3]]

    fortune_cookie = FortuneCookie(fortune_list, (2, "좋음"))
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()