class Solution(object):
    def closestPrimes(self, left, right):
        # Generate all prime numbers up to right using Sieve of Eratosthenes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                is_prime[i*i:right+1:i] = [False] * len(range(i*i, right+1, i))

        # Collect all primes in the range [left, right]
        primes_in_range = [i for i in range(max(left, 2), right + 1) if is_prime[i]]

        # Find the closest pair of primes
        if len(primes_in_range) < 2:
            return [-1, -1]

        return min(((primes_in_range[i], primes_in_range[i+1]) for i in range(len(primes_in_range) - 1)), key=lambda x: x[1] - x[0])