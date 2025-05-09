# Author: Eva Peck
# Date: 3/1/25
# Purpose: Compound Interest

# Input

# PV
fStartPrincipal = float(input("Enter the starting principal: "))
# R
fAnnualInterest = float(input("Enter the annual interest rate: "))
# m
iCompounding = int(input("How many times per year is the interest compounded? "))
# t
iYears = int(input("How many years will the account earn interest? "))

# Calculations

fFutureValue = fStartPrincipal * (1.0 + (fAnnualInterest / 100) / iCompounding) \
               ** (iCompounding * iYears)

# Output

print(f"At the end of {iYears} years you will have ${fFutureValue:,.2f}")
