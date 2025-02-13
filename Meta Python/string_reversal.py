# str[start:stop:step] slice functin

my_list = "Drinnk coffee"
new_list = my_list[::-1]
print(new_list)
print(my_list)


# recursive reverse
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
str = "reversal"
reverse = string_reverse(str)
print(reverse)


def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(6))  # Output: 8
