# collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show to the user

def main():
    print("Monthly Payment Loan Calculator")
    print("")

    principal = float(input("Enter loan amount > "))
    apr = float(input("Enter annual interest rate > "))
    years = int(input("Enter amount of years > "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("Monthly Payment > %.2f" % monthly_payment)

main()