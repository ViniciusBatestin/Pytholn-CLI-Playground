# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b=[0] * len(a)

for i in range(len(a)):
    b[i] = a[i]

print(b)

b[0] = 99
print(b)
print(a)

###################################################
# Explanation

'''
I could use b = a.copy() but i reather practice the loop in range
Create a global var b and assing to it 1 index times length of a
Iterates over a and copy the index elemts from a to b
'''
