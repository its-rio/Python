#write script in python to generate first 20 prime numbers with atleart 3 digit

def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

count = 0
number = 100  # Starting from 100 to ensure at least 3 digits
prime_numbers = []

while count < 20:
    if prime(number):
        prime_numbers.append(number)
        count += 1
    number += 1

for prime in prime_numbers:
    print(prime)

          
