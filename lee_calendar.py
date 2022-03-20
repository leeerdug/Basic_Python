import datetime

now = datetime.datetime.now()
weekday = datetime.datetime.today().weekday()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))

year = now.year % 12
weekdays  = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

if year == 0:
    print("현재 연도는 {}년으로 원숭이의 해입니다!".format(now.year))
elif year == 1:
    print("현재 연도는 {}년으로 닭의 해입니다!".format(now.year))
elif year == 2:
    print("현재 연도는 {}년으로 개의 해입니다!".format(now.year))
elif year == 3:
    print("현재 연도는 {}년으로 돼지의 해입니다!".format(now.year))
elif year == 4:
    print("현재 연도는 {}년으로 쥐의 해입니다!".format(now.year))
elif year == 5:
    print("현재 연도는 {}년으로 소의 해입니다!".format(now.year))
elif year == 6:
    print("현재 연도는 {}년으로 호랑이의 해입니다!".format(now.year))
elif year == 7:
    print("현재 연도는 {}년으로 토끼의 해입니다!".format(now.year))
elif year == 8:
    print("현재 연도는 {}년으로 용의 해입니다!".format(now.year))
elif year == 9:
    print("현재 연도는 {}년으로 뱀의 해입니다!".format(now.year))
elif year == 10:
    print("현재 연도는 {}년으로 말의 해입니다!".format(now.year))
elif year == 11:
    print("현재 연도는 {}년으로 양의 해입니다!".format(now.year))

if 3 <= now.month <= 5:
    print("현재 계절은 {}월로 봄입니다!".format(now.month))
elif 6 <= now.month <= 8:
    print("현재 계절은 {}월로 여름입니다!".format(now.month))
elif 9 <= now.month <= 11:
    print("현재 계절은 {}월로 가을입니다!".format(now.month))
else:
    print("현재 계절은 {}월로 겨울입니다!".format(now.month))

if 1 <= now.day <= 10:
    print("현재 날짜는 {}일로 {}월 초입니다!".format(now.day,now.month))
elif 11 <= now.day <= 20:
    print("현재 날짜는 {}일로 {}월 중순입니다!".format(now.day,now.month))
else:
    print("현재 날짜는 {}일로 {}월 말입니다!".format(now.day,now.month))

print("현재 요일은 {}입니다.".format(weekdays[weekday]))

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
else:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
