n = 1260                        #총금액
count = 0                       #거스름돈으로 줄 동전 갯수
coin_list = [500, 100, 50, 10]  #돈 종류 배열

for coin in coin_list:          #배열 coin_list의 돈 종류를 coin으로 반복
    count += n // coin          #갯수 = 금액 / coin
    n %= coin                   #잔액 = 금액 % coin

print(count)                    #출력
