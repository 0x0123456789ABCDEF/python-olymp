input()
a = sorted(map(int, input().split(' ')))
res = int((a[-1] + a[-2])/2)
print(res)