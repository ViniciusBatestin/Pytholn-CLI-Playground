# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.
def name_and_age(name, age):
    if age > 0:
        return(name + " is " + str(age) + " years old.")
    else:
        return("Error: Invalid age")

###################################################
# Tests
# Student should not change this code.

def test(name, age):
	"""Tests the name_and_age function."""

	print(name_and_age(name, age))

test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age
