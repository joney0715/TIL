#테스트 데이터 입력
T = int(input('Input T: '))
Input = []
for i in range(T):
    word = input()
    Input.append(word)

#풀이
def solution(Input):
    for T in range(len(Input)):
        if Input[T] == Input[T][::-1] : #본래 단어와 비교
            print(f'#{T+1}', 1) #회문인 경우 1 출력
        else:
            print(f'#{T+1}', 0)
    
#결과 출력
solution(Input)

