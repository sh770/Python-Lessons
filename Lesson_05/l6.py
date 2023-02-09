import random
import time

def random_until_six():
    numbers = []
    count = [0] * 20
    start_time = time.time()
    while len(numbers) < 20:
        num = random.randint(1, 20)
        if num not in numbers:
            numbers.append(num)
        count[num - 1] += 1
        print(f'Generated number: {num}')
    
    end_time = time.time()
    print('\nFrequency of each number:')
    for i in range(1, 21):
        print(f'{i}: {count[i - 1]}')
    print(f'\nTotal time: {end_time - start_time:.2f} seconds')
    input("Press Enter to exit")

random_until_six()