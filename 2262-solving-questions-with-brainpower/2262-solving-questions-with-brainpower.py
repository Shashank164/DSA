class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        res = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            res[i] = max(points + (res[next_q] if next_q < n else 0), res[i + 1])

        return res[0]