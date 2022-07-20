#N = 7
#LHs = [0,0,4,0,6,3,0,0,10,0,0,4,0,6,0,8]
#LHs = [(2, 4),(11, 4),(15, 8),(4, 6),(5, 3),(8, 10),(13, 6)]



N = int(input())
LHs = []
for i in range(N):
    (l, h) = map(int, input().split())
    LHs.append((l,h))


LHs.sort()
H_max = 0
id_max = 0
for idx, LH in enumerate(LHs):
    if LH[1] > H_max:
        H_max = LH[1]
        id_max = idx
        
def solution(LHs):
    area = H_max
    s_r = (LHs[id_max+1][0] - LHs[id_max][0]) * LHs[id_max+1][1]
    s_l = (LHs[id_max][0] - LHs[id_max-1][0]) * LHs[id_max-1][1]
    for i in range(id_max+2, len(LHs)):
        if LHs[i][1] > LHs[i-1][1]:
            s_r = (LHs[i][0] - LHs[id_max][0]) * LHs[i][1]
        else:
            s_r += (LHs[i][0] - LHs[i-1][0]) * LHs[i][1]

    for j in range(id_max-2, -1, -1):
        if LHs[j][1] > LHs[j+1][1]:
            s_l = (LHs[id_max][0] - LHs[j][0]) * LHs[j][1]
        else:
            s_l += (LHs[j+1][0] - LHs[j][0]) * LHs[j][1]

    return H_max + s_r + s_l
        
print(solution(LHs))

'''
최대치가 맨 왼쪽이나 맨 오른쪽인 경우
'''








