T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies_map = []
    for _ in range(N):
        flies = list(map(int, input().split()))
        flies_map.append(flies)

    dead_flies = []
    for i in range(N):
        for j in range(N):
            if i <= N - M and j <= N - M:
                dead_fly = 0
                for x in range(0,M):
                    for y in range(0,M):
                        dead_fly += flies_map[i+x][j+y]

            dead_flies.append(dead_fly)

    answer = max(dead_flies) 
    print(f'#{test_case}', answer)