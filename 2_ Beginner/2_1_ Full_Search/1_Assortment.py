def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

max_n = 10 ** 5
memo = [0]*(max_n + 1)
def fib(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

