n = int(input())
a = [int(i) for i in input().split()]

#Longest bar < sum other bar

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            len = a[i] + a[j] + a[k]
            ma = max(a[i], a[j], a[k])
            rest = len - ma
            if ma < rest:
                ans = max(ans, len)

print(ans)