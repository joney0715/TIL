D = []
for _ in range(9):
    d = int(input())
    D.append(d)


D.sort()
D_sum = sum(D)
t1, t2 = 0, 0 

for i in range(9): 
    D_s = D_sum
    D_s -= D[i]
    for j in range(i+1,9):
        D_ss = D_s - D[j]
        if D_ss == 100:
            t1 = i
            t2 = j
            break

answer = []
for a in range(9):
    if a == t1 or a  == t2:
        continue
    answer.append(D[a])

for ans in answer:
    print(ans)

