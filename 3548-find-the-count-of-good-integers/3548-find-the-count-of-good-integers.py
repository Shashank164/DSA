from math import factorial
class Solution(object):
    def countGoodIntegers(self, n, k):
        s = set()
        if n == 1:
            for d in range(1, 10):
                if d % k == 0:
                    cnt = [0] * 10
                    cnt[d] = 1
                    s.add(tuple(cnt))
        else:
            if n % 2 == 0:
                h = n // 2
                for i in range(10**(h - 1), 10**h):
                    t = str(i)
                    p = t + t[::-1]
                    if int(p) % k == 0:
                        cnt = [0] * 10
                        for c in p:
                            cnt[ord(c) - 48] += 1
                        s.add(tuple(cnt))
            else:
                h = n // 2
                for i in range(10**(h - 1), 10**h):
                    t = str(i)
                    for m in range(10):
                        p = t + str(m) + t[::-1]
                        if int(p) % k == 0:
                            cnt = [0] * 10
                            for c in p:
                                cnt[ord(c) - 48] += 1
                            s.add(tuple(cnt))

        ans = 0
        fact = [factorial(i) for i in range(n + 1)]
        for cnt in s:
            tot = fact[n]
            for c in cnt:
                tot //= fact[c]
            if cnt[0]:
                prod = 1
                for d in range(1, 10):
                    prod *= fact[cnt[d]]
                inv = fact[n - 1] // (fact[cnt[0] - 1] * prod)
            else:
                inv = 0
            ans += tot - inv
        return ans