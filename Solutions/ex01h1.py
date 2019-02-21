from bisect import bisect_right as bs
ls = [0, 1, 3]
while ls[-1] < 2e9:
    ls.append(ls[-1] + bs(ls, len(ls) - 1))
for _ in range(int(input())):
    print(bs(ls, int(input()) - 1))
