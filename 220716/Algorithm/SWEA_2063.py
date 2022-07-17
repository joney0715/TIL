#테스트 케이스 입력
N = int(input('Input N in odd numbers : '))
Input = list(map(int, input(f'Input {N} numbers : ').split()))

#풀이
def solution(Input):
    Input.sort() #리스트 정렬
    m = len(Input) // 2 #중앙값의 인덱스 계산
    return Input[m] 

#결과 출력
print(solution(Input))

