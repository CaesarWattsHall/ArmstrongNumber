def is_armstrong_number(number):
    # Convert the number to a string to get the number of digits (n)
    number_str = str(number)
    n = len(number_str)

    # Calculate the sum of the nth powers of the digits
    sum_of_powers = 0
    for digit_str in number_str:
        digit = int(digit_str)
        sum_of_powers += digit ** n

    # Check if the sum of the nth powers of the digits is equal to the original number
    return sum_of_powers == number

# Read lines from standard input
for line in sys.stdin:
    # Convert the line to an integer
    number = int(line.strip())

    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print("True")
    else:
        print("False")
