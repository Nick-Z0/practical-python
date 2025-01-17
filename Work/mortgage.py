# Exercise 1.17
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0
    principal = principal * (1+rate/12) - payment - extra
    total_paid = total_paid + payment + extra
    month = month + 1
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(f'{month} \t {total_paid:0.2f} \t {principal:0.2f}')

print(f'Total paid      {total_paid:0.2f}')
print(f'Total months    {month}')
