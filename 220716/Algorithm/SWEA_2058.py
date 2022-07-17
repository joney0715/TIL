import random
#테스트 데이터 입력
#N = random.randint(1,9999) #랜덤한 테스트 데이터 생성
N = int(input('Input N (1 ≤ N ≤ 9999): '))

#풀이
def solution(N):
    N = [int(i) for i in str(N)] #각 자리의 숫자를 리스트에 넣기
    answer = sum(N) #총합 계산
    return answer

#결과 출력
print(solution(N))