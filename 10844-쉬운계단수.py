import sys
sys.stdin = open('input.txt', 'r')

MOD = 1_000_000_000

# cache[n][d]: 길이가 n, 마지막 숫자가 d인 계단수 개수
cache = [[0]*10 for _ in range(101)]
for i in range(1, 10):
    cache[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i-1][j-1]
        if j <9:
            cache[i][j] += cache[i-1][j+1]

ans = 0    
N = int(input())
for i in range(10):
    ans += cache[N][i]
    ans %= MOD
print(ans)
