# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.
def print_digits(number):
    if (number >= 0) and (number < 100):
        tens = str(number // 10)
        ones = str(number % 10)
        print("The tens digit is " + tens + ", and the ones digit is " + ones + ".")
    else:
        print("Error: Input is not a two-digit number.")


###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.
