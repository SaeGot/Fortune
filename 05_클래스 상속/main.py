from FortuneCookie import FortuneCookie

if __name__ == '__main__':
    fortune_list = [["좋음", 3], ["보통", 2], ["나쁨", 1]]

    fortune_cookie = FortuneCookie(fortune_list)
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()
    fortune_cookie.SelectFortune()