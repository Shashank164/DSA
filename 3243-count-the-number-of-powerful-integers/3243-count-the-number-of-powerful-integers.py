class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def count_valid_numbers(n):
            s_str = str(s)
            s_len = len(s_str)
            n_str = str(n)
            n_len = len(n_str)
            count = 0

            # Case 1: Numbers shorter than s cannot end with s
            if n_len < s_len:
                return 0

            # Case 2: Numbers exactly as long as s
            if n_len == s_len:
                if int(s) <= n and all(int(d) <= limit for d in s_str):
                    return 1
                else:
                    return 0

            # Case 3: Numbers longer than s
            max_prefix = (n - int(s)) // (10 ** s_len)
            if max_prefix < 0:
                return 0

            prefix_str = str(max_prefix)
            prefix_len = len(prefix_str)

            # Manual memoization (replaces lru_cache)
            memo = {}

            def dfs(pos, tight, is_zero):
                if pos == prefix_len:
                    return 0 if is_zero else 1
                key = (pos, tight, is_zero)
                if key in memo:
                    return memo[key]

                max_digit = int(prefix_str[pos]) if tight else 9
                total = 0
                for d in range(0, max_digit + 1):
                    if d > limit:
                        continue
                    new_tight = tight and (d == max_digit)
                    new_is_zero = is_zero and (d == 0)
                    if new_is_zero:
                        total += dfs(pos + 1, new_tight, new_is_zero)
                    else:
                        total += dfs(pos + 1, new_tight, False)
                memo[key] = total
                return total

            count_prefix = dfs(0, True, True)
            # Include the case where prefix is 0 (the number is s itself)
            if int(s) <= n and all(int(d) <= limit for d in s_str):
                count_prefix += 1
            return count_prefix

        total = count_valid_numbers(finish) - count_valid_numbers(start - 1)
        return total