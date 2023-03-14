# Define the inputs
property_value = float(input("Enter the property value (in USD): ").replace(",", ""))
net_operating_income = float(input("Enter the net operating income (in USD): ").replace(",", ""))

# Calculate the cap rate
cap_rate = net_operating_income / property_value

# Display the results
print("The cap rate is: {:.2%}".format(cap_rate))

# Define the inputs
down_payment = float(input("Enter the down payment amount (in USD): ").replace(",", ""))
closing_costs = float(input("Enter the closing costs (in USD): ").replace(",", ""))
net_operating_income = float(input("Enter the net operating income (in USD): ").replace(",", ""))
mortgage_payment = float(input("Enter the monthly mortgage payment (in USD): ").replace(",", ""))
holding_period = int(input("Enter the holding period (in years): "))

# Calculate the cash on cash return
total_investment = down_payment + closing_costs
total_cash_flow = net_operating_income - (mortgage_payment * 12)
cumulative_cash_flow = total_cash_flow * holding_period
cash_on_cash_return = cumulative_cash_flow / total_investment

# Display the results
print("The cash on cash return is: {:.2%}".format(cash_on_cash_return))