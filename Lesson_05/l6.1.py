import random
import time

def random_until_limit():
    limit = int(input("Enter the upper limit of the numbers: "))
    numbers = []
    count = [0] * limit
    start_time = time.time()
    while len(numbers) < limit:
        num = random.randint(1, limit)
        if num not in numbers:
            numbers.append(num)
        count[num - 1] += 1
        print(f'Generated number: {num}')
    
    end_time = time.time()
    print('\nFrequency of each number:')
    for i in range(1, limit + 1):
        print(f'{i}: {count[i - 1]}')
    print(f'\nTotal time: {end_time - start_time:.2f} seconds')
    input("Press Enter to exit")

random_until_limit()
