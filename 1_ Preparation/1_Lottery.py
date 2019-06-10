n = int(input())
m = int(input())
k = [int(i) for i in input().split()]

#max_n = 50
f = False

for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if k[a] + k[b] + k[c] + k[d] == m:
                    f = True

print("Yes" if f else "No")