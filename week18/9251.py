s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

m = [[0] * (l2+1) for _ in range(l1 +1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            m[i+1][j+1] = m[i][j] + 1
        else:
            m[i+1][j+1] = max(m[i][j+1], m[i+1][j])

print(m[l1][l2])