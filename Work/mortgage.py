# mortgage.py
#
# Exercise 1.7
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
    month += 1
    
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    
    if total_payment > principal:
        total_payment = principal
        principal = 0
    else:    
        principal = principal * (1+rate/12) - total_payment 
    
    total_paid = total_paid + total_payment
    print(month, "\t", round(total_paid,2), "\t", round(principal,2))

print('Months', month)
print('Total paid', total_paid)
