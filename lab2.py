def prime_num_generator():
    for n in range(2, 102):  # n starts from 2 to end
        for x in range(2, n):  # check if x can be divided by n
            if n % x == 0:  # if true then n is not prime
                break
        else:  # if x is found after exhausting all values of x
            yield n
        n += 1


a = prime_num_generator()
print(next(a))
print(next(a))

