# program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Enter a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

sum_of_digits = str(first_digit + second_digit)

print("Sum of the digits: " + sum_of_digits)