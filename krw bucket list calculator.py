# Ask the user for their salary in any currency
salary_input=input("Enter your expected monthly salary in any currency: ")
monthly_salary=int(salary_input)
# Ask the user for their monthly living costs in any currency
expenses_input=input("Enter your estimated monthly expenses in any currency: ")
monthly_expenses= int(expenses_input)
# calculate the monthly savings using subtraction
monthly_savings= monthly_salary - monthly_expenses
# calculate total savings for a month

# calculate total savings for a whole year using multiplication
yearly_savings=monthly_savings * 12
# print the exiciting results to the screen
print("\n======== YOUR FINANCIAL GRAPH ========"
)
print(f"Every month, you will save: {monthly_savings:,} in your country currency")

print(f"In one single year, you will save: {yearly_savings:,} in your country currency!")
