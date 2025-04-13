import time
import matplotlib.pyplot as plt
import math

# === Prime Check Function ===
def is_prime(n):
    if n < 2:
        return False, 0
    steps = 1  # initial step for checking n < 2
    if n == 2:
        return True, steps
    if n % 2 == 0:
        steps += 1
        return False, steps

    steps += 1  # for the even check
    sqrt_n = int(math.sqrt(n)) + 1

    for i in range(3, sqrt_n, 2):
        steps += 1
        if n % i == 0:
            return False, steps

    return True, steps

# === Graph Drawing Function ===
def draw_prime_graphs(digits, step_counts, time_taken):
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5))

    # Steps graph
    left.plot(digits, step_counts, marker='o', color='green', label='Steps')
    left.set_title("Steps vs. Number of Digits (Prime Check)")
    left.set_xlabel("Digits in Number")
    left.set_ylabel("Steps Taken")
    left.grid(True)
    left.legend()

    # Time graph
    right.plot(digits, time_taken, marker='s', color='purple', label='Time (s)')
    right.set_title("Time vs. Number of Digits (Prime Check)")
    right.set_xlabel("Digits in Number")
    right.set_ylabel("Time (seconds)")
    right.grid(True)
    right.legend()

    plt.tight_layout()
    plt.show()

# === Collect and Process Data ===
digits_list = []
steps_list = []
times_list = []

# Generate test numbers with increasing digit counts
for num_digits in range(1, 10):  # 1 to 9 digits
    test_number = 10**(num_digits - 1) + 1  # e.g., 11, 101, 1001, etc.

    start_time = time.time()
    is_p, steps = is_prime(test_number)
    end_time = time.time()

    time_taken = end_time - start_time

    digits_list.append(num_digits)
    steps_list.append(steps)
    times_list.append(time_taken)

    print(f"{test_number}: Prime={is_p}, Steps={steps}, Time={time_taken:.8f} seconds")

# === Draw Graphs ===
draw_prime_graphs(digits_list, steps_list, times_list)
