n, m, k = map(int, input().split())     #N, M, K를 공백으로 입력
data = list(map(int, input().split()))   #N개의 수를 공백으로 입력

data.sort()                             #N개의 수 정렬

first = data[n-1]                       #가장 큰 수
second = data[n-2]                      #두 번째로 큰 수
#가장 큰 수가 더해지는 수
count = int(m / (k+1)) * k              #m이 k+1로 나눠질 경우
count += m % (k+1)                      #m이 k+1로 나눠지지 않을 경우

result = 0                              #결과값 result
result += count * first                 #가장 큰 수를 count만큼 더함
result += (m - count) * second          #두 번째 큰 수를 m - count만큼 더함

print(result)
