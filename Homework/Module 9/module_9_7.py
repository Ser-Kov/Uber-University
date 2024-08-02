import sympy


def is_prime(func):
    def wrapper():
        result = func()
        if sympy.isprime(result):
            print('Простое')
        else:
            print('Составное')
    return wrapper()


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)