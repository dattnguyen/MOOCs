# balance = float(input('please enter balance:'))
# AIR = float(input('please enter annual interest rate as a decimal:'))
# MPR = float(input('please enter monthly payment rate as a decimal'))
balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
MIR = annualInterestRate/12

for x in range(1,13):
    min_month_pay = monthlyPaymentRate * balance
    month_unpaid_balance = balance - min_month_pay
    balance = month_unpaid_balance + MIR * month_unpaid_balance
balance = '{:.2f}'.format(balance)
print('Remaining balance:', balance)
#%%
balance = 4773
b0 = balance # we need a variable to hold the balance so that after each while loop we can use it
annualInterestRate = 0.2
min_month_pay = 0
MIR = annualInterestRate/12
while True:
    for x in range(1, 13): #this is to calculate the new balance
        month_unpaid_balance = balance - min_month_pay
        balance = month_unpaid_balance * (1 + MIR)
    if balance < 0:
        print('Lowest Payment: ', min_month_pay)
        break
    else:
        min_month_pay += 10
        balance = b0 #we need this because after the first loop, the balance has been changed

#%%
balance = 4773
b0 = balance # we need a variable to hold the balance so that after each while loop we can use it
annualInterestRate = 0.2
min_month_pay = 0
MIR = annualInterestRate/12.0
upper_bound = (b0*(1+MIR)**12)/12 #upper bound is when we have to pay the whole amount that accumulates for 12 months
lower_bound = b0/12 #lower bound is when we pay 1/12, but still need to pay interest
while True:
    for x in range(1, 13): #this is to calculate the new balance
        month_unpaid_balance = balance - min_month_pay
        balance = month_unpaid_balance * (1 + MIR)
    if abs(balance) < 0.1:
        print('Lowest Payment: ', round(min_month_pay,2))
        break
    else:
        if balance > 0: #if balance is greater than 0 we don't pay enough, need to increase lower bound
            lower_bound = min_month_pay
        elif balance <0: #if balance is smaller than 0, we pay too much, need to reduce the upper bound
            upper_bound = min_month_pay

        min_month_pay = (lower_bound + upper_bound)/2
        balance = b0 #we need this because after the first loop, the balance has been changed
