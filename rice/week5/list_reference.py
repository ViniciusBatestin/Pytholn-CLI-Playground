# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0
print (a)
print (b)


###################################################
# Explanation

# The assignment b = a created a second reference to a.
# Setting b[0] = 0 also mutated the list that both
# a and b reference.  As a result, a[0] == 0.

# See the Programming Tips videos for a more detail
# explanation and examples
