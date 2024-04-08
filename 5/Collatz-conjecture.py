# Implementation of the script for the Collatz conjecture
def collatz_sequence(n):
    """Generates the Collatz sequence for a given number n and returns the process as a string."""
    process_str = ""
    while n != 1:
        if n % 2 == 0:  # Even
            next_n = n // 2
            process_str += f"{n} (even) > "
        else:  # Odd
            next_n = 3 * n + 1
            process_str += f"{n} (odd) > "
        n = next_n
    process_str += "1 (odd)"  # Adding the final part of the process
    return process_str

# Main loop to keep taking inputs and showing the Collatz sequence process
def main():
    while True:
        try:
            user_input = input("Enter a positive integer (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
            number = int(user_input)
            if number <= 0:
                raise ValueError
            process = collatz_sequence(number)
            print(process)
        except ValueError:
            print("Please enter a valid positive integer.")

# Uncomment the following line to run the script
main()
