import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))

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

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
else:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
