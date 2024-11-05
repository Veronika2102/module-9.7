
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_t = sum(args)
        p = 0
        for i in range(2, sum_t // 2 + 1):
            if sum_t % i == 0:
                p = p +1
        if p <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper
@is_prime
def sum_three(*args):
    return sum(args)



result = sum_three(6, 11, 8)
print(result)