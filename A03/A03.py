# Write your code here:

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️
# revenue : 수익
# expenses : 지출
# tax_credits : 세액 공제(할인)율
# tax_amount : 세액

# get_tax_amount는 if/else를 사용할 것
# if (profit > 100,000) -> tax_credits = 0.25
# else -> tax_credits = 0.15

# get_yeraly_revenue : 연간 매출 계산
# get_yearly_expenses : 연간 지출 계산
# get_tax_amount : 세액 계산
# apply_tax_credits : 세액 - 할인금액

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


def get_yearly_revenue(montly_revenue):
  return montly_revenue * 12

def get_yearly_expenses(monthly_expenses):
  return monthly_expenses * 12
profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

def get_tax_amount(profit):
  if profit > 100000:
    return profit * 0.25
  else:
    return profit * 0.15
tax_amount = get_tax_amount(profit)

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount * tax_credits
final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")