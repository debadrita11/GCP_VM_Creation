import multiprocessing
import time

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes():
    """Continuously generate prime numbers."""
    num = 2
    while True:
        if is_prime(num):
            print(num, end=" ", flush=True)  # Print primes continuously
        num += 1

def stress_test(cpu_cores):
    """Run prime number generation on multiple CPU cores."""
    processes = []
    for _ in range(cpu_cores):
        p = multiprocessing.Process(target=generate_primes)
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)  # Keep running indefinitely
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        print("\nStress test stopped.")

if __name__ == "__main__":
    cpu_cores = multiprocessing.cpu_count()  # Get the number of CPU cores
    print(f"Starting stress test on {cpu_cores} cores...")
    stress_test(cpu_cores)