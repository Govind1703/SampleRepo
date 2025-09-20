def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2  # Start checking from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Main program
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of prime numbers you want: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            primes = first_n_primes(n)
            print(f"The first {n} prime numbers are:")
            print(primes)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")