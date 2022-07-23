
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        record = list(map(int, input().split()))
        matrix.append(record)

    answer = []
    for i in range(N):
        ans_re = ['','','']
        for j in range(N):
            ans_re[0] += str(matrix[N-j-1][i])
            ans_re[1] += str(matrix[N-i-1][-1-j])
            ans_re[2] += str(matrix[j][-1-i])
        answer.append(ans_re)

    print(f'#{test_case}')
    for a in answer:
        for i,b in enumerate(a):
            if i == 2:
                print(b)
            else:
                print(b, end=' ')
