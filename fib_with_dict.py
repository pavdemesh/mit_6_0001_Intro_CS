def fib_w_dict(n, already_calculated):
    if n in already_calculated:
        return already_calculated[n]
    else:
        ans = fib_w_dict(n - 1, already_calculated) + fib_w_dict(n - 2, already_calculated)
        already_calculated[n] = ans
        return ans


fibonacci_values = {1: 1, 2: 2}

print(fib_w_dict(25, fibonacci_values))
