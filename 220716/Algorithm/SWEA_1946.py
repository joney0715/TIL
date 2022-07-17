#테스트 케이스 생성
t = int(input('Input T: ')) #테스트 케이스 개수
test_cases = [0] * (t)
for case in range(t):
    #압축 결과 입력 
    test_cases[case] = []
    N = int(input('Input the number of alphabet: ')) #알파벳 개수
    for i in range(N):
        C, K = map(str, input().split())
        test_cases[case].append((C,int(K)))

#풀이 알고리즘
def solution(test_cases):
    #테스트 케이스 하나씩 처리
    for i in range(len(test_cases)): 
        print(f'#{i+1}') #테스트 케이스 번호 출력

        #압축 풀기
        answer = '' #결과값 초기화
        for alphabet in test_cases[i]:
            answer += alphabet[0] * alphabet[1] # 압출을 풀어서 한줄로 표현

        #너비에 맞게 표현
        end = len(answer)//10 #너비로 나눠서 행 수 계산
        start = 0
        for j in range(end):
            print(answer[start:start+10]) #한 줄씩 출력
            start += 10
        print(answer[10*end:]) #나머지 출력

#결과값 출력
solution(test_cases)