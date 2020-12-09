counter = [0]


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        # if counter[0] % 1_000_000_000 == 0:
        #     print("one more billion operations")
        counter[0] += 1
        return fib(x-1) + fib(x-2)


# print(fib(5))
# print(fib(15))
# print(fib(25))
print(fib(20))

print(counter[0])
