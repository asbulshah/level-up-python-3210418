def get_prime_factors(numbers):
    factors = [1]
    divisor = 2

    while divisor <= numbers :
        if numbers % divisor == 0:
            factors.append(divisor)
            numbers = numbers // divisor
        else:
            divisor = divisor+1
    return factors


if __name__ == "__main__":
    num = int(input("Enter a number:\n"))
    print(get_prime_factors(num))
