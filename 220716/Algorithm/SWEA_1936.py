#테스트 케이스 입력
A, B = map(int, input().split())

#풀이
def solution(A,B):
    # 비기는 경우 (요구사항에는 없었음)
    if A == B:
        return 'draw'

    #승패가 갈린 경우
    B = B % 3 #3으로 나눈 나머지 계산
    if A == B+1: #A와 같으면 A승리
        answer = "A"
    else:
        answer = "B"

    return answer

#결과 출력
print(solution(A,B))