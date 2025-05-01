class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        import bisect
        def can(k):
            arr = workers[:]
            p = pills
            for t in reversed(tasks[:k]):
                i = bisect.bisect_left(arr, t)
                if i < len(arr):
                    arr.pop(i)
                else:
                    if p == 0:
                        return False
                    j = bisect.bisect_left(arr, t - strength)
                    if j < len(arr):
                        arr.pop(j)
                        p -= 1
                    else:
                        return False
            return True
        l, r = 0, min(len(tasks), len(workers))
        while l < r:
            mid = (l + r + 1) // 2
            if can(mid):
                l = mid
            else:
                r = mid - 1
        return l