class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        t = sorted(enumerate(nums), key=lambda x: x[1])
        group, grou_i = [], []

        for i in range(len(t)):
            if group and t[i][1] - group[-1] > limit:
                for j in sorted(grou_i):
                    nums[j] = group.pop(0)
                group, grou_i = [], []
            group.append(t[i][1])
            grou_i.append(t[i][0])

        for j in sorted(grou_i):
            nums[j] = group.pop(0)

        return nums