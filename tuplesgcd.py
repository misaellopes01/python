import sys
from math import gcd
k = int(sys.stdin.readline())

score = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            score += gcd(gcd(a,b),c)
print(score)