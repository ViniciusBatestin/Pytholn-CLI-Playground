'''
FIND F(X)

def f(x):
     return -5 * x**5 + 69 * x**2 - 47

f_0 = f(0)
f_1 = f(1)
f_2 = f(2)
f_3 = f(3)

print(f_0, f_1, f_2, f_3)

maximal = max(f_0, f_1, f_2, f_3)

print(maximal)'''

'''
FUTURE VALUE FORMULA

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return present_value * (1 + rate_per_period)**periods

print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))
print(future_value(500, .04, 10, 10))'''
