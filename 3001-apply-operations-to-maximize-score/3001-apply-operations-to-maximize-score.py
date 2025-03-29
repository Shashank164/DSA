def primeFactors(n):
    i = 2
    ans = set()
    while i * i <= n:
        while n % i == 0:
            ans.add(i)
            n //= i
        i += 1
    if n > 1:
        ans.add(n)
    return len(ans)

class Solution:
    def maximumScore(self, nums, k):
        mod = 10**9 + 7
        n = len(nums)
        arr = [(i, primeFactors(x), x) for i, x in enumerate(nums)]
        left, right, stk = [-1] * n, [n] * n, []

        for i, f, _ in arr:
            while stk and arr[stk[-1]][1] < f:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i, f, _ in reversed(arr):
            while stk and arr[stk[-1]][1] <= f:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)

        arr.sort(key=lambda x: -x[2])
        ans = 1
        for i, _, x in arr:
            cnt = (i - left[i]) * (right[i] - i)
            use = min(cnt, k)
            ans = ans * pow(x, use, mod) % mod
            k -= use
            if k == 0:
                break
        return ans