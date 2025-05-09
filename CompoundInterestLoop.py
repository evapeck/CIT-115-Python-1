# CompoundInterestLoop
# CIT-115
# 4/8/25
# Eva Peck

# Deposit input, check for negative #s and invalid characters
fDeposit = 0
while fDeposit <= 0: # while deposit is less than/equal to 0, do this
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit <= 0: # User entered 0 or less
            print("Input must be a positive numeric value")
    except ValueError: # User entered invalid character
        print("Input must be a positive numeric value")

# Interest rate input, check for negative #s and invalid characters
fInterestRate = 0
while fInterestRate <= 0: # while interest rate is less than/equal to 0, do this
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
        if fInterestRate <= 0: # User entered 0 or less
            print("Input must be a positive numeric value")
    except ValueError: # User entered invalid character
        print("Input must be a positive numeric value")

# Month input, check for negative #s and invalid characters
iMonths = 0
while iMonths <= 0: # while month is less than/equal to 0, do this
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0: # User entered 0 or less
            print("Input must be a positive numeric value")
    except ValueError: # User entered invalid character
        print("Input must be a positive numeric value")

# Goal input, check for #s less than 0
fGoal = -1
while fGoal < 0: # while goal is less than 0, do this
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0: # User entered less than 0
            print("Input must be 0 or greater")
    except ValueError: # User entered invalid character
        print("Input must be a positive numeric value")

# Initialize/Assign Variables
fMonthlyRate = fInterestRate / 100 / 12
fAccountBalance = fDeposit

# Loop through and print out each month's results
for iMonth in range(1, iMonths + 1): # for as many months entered, do this
    fAccountBalance += fAccountBalance * fMonthlyRate # for each iteration, add balance times monthly rate
    print(f"Month: {iMonth} \t Account Balance is: ${fAccountBalance:,.2f}" )
    iMonth += 1 # Move onto next month iteration


if fGoal > 0 and fDeposit < fGoal: # Goal is greater than 0 and greater than the deposit amt
    iMonth = 0
    while fDeposit <= fGoal: # while deposit is less than/equal to goal, do this
        fDeposit += fDeposit * fMonthlyRate # for each iteration, add deposit times monthly rate
        iMonth += 1 # Move onto next month iteration
    print(f"It will take: {iMonth} months to reach the goal of ${fGoal:,.2f}")




