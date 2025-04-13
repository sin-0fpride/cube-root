import time
import matplotlib.pyplot as plt

# === Cube Root Function ===
def simple_cube_root(n):
    steps = 0
    is_negative = n < 0
    n = abs(n)
    low = 0
    high = n
    precision = 1e-10

    while (high - low) > precision:
        steps += 1
        mid = (low + high) / 2
        cube = mid * mid * mid

        if cube < n:
            low = mid
        else:
            high = mid

    result = (low + high) / 2
    return -result if is_negative else result, steps

# === Graph Drawing Function ===
def draw_graphs(digits, step_counts, time_taken):
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5))

    # Steps graph
    left.plot(digits, step_counts, marker='o', color='blue', label='Steps')
    left.set_title("Steps vs. Number of Digits")
    left.set_xlabel("Digits in Number")
    left.set_ylabel("Steps Taken")
    left.grid(True)
    left.legend()

    # Time graph
    right.plot(digits, time_taken, marker='s', color='red', label='Time (s)')
    right.set_title("Time vs. Number of Digits")
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

# Test numbers with increasing digit lengths
for num_digits in range(1, 11):  # From 1-digit to 10-digit numbers
    test_number = 10**(num_digits - 1) + 5  # e.g., 15, 105, 1005...

    start_time = time.time()
    _, steps = simple_cube_root(test_number)
    end_time = time.time()

    time_taken = end_time - start_time

    digits_list.append(num_digits)
    steps_list.append(steps)
    times_list.append(time_taken)

    print(f"{test_number}: Steps={steps}, Time={time_taken:.8f} seconds")

# === Draw Graphs ===
draw_graphs(digits_list, steps_list, times_list)
