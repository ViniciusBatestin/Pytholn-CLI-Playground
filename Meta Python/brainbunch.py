# class A:
#    def a(self):
#        return "Function inside A"

# class B:
#    def a(self):
#        return "Function inside B"

# class C:
#    pass

# class D(C, A, B):
#    pass

# d = D()
# print(d.a())

start_balance = 0
days_of_june = {1: 1223,
                10: 615,
                15: -63,
                22: -120,
                30: 0}

def balance(start_balance, days_of_june):
    daily_balance = []
    current_balance = start_balance

    for day in range(1, 31):
        if day in days_of_june:
            current_balance += days_of_june[day]
        daily_balance.append(current_balance)

    average_balance = sum(daily_balance) / 30
    return average_balance

# expect return of 1583,90
average_balance = balance(start_balance, days_of_june)
print(f"Average balance for june: {average_balance}")
