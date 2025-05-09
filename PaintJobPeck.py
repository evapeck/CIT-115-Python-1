# Eva Peck
# CIT 115-D02
# 4/25/25
# PAINT JOB w Functions and Output Files

from math import ceil

def getFloatInput(sPrompt): # Converts string prompt into float
    iNumber = 0
    while iNumber <= 0:
        try:
            iNumber = float(input(sPrompt))
            if iNumber <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid number that is > 0.")
    return iNumber

def getGallonsOfPaint(fSqFtIn, fFeetPerGalIn): #how many gal needed, rounded up to next gal
    # Find float value of gallons required
    return ceil(fSqFtIn / fFeetPerGalIn)
    # Find actual number gallons needed (round up if not whole number)
    # send gallons needed for usage

def getLaborHours(fLaborHoursPerGalIn, iTotalGal): # find how many hours it will take to paint
    # Find total labor hours by multiplying labor hours per gallon and total gallons
    return fLaborHoursPerGalIn * iTotalGal
    # send total labor hours for usage

def getLaborCost(fLaborHoursPerGalIn, fLaborPerHourIn): # find how much labor will cost to paint
    # Find total labor cost by multiplying labor hours per gallon and labor cost per gallon
    return fLaborHoursPerGalIn * fLaborPerHourIn
    # send total labor cost for usage

def getPaintCost(fPaintCostPerGalIn, iTotalGal): # find how much the required paint will cost
    # find paint cost by multiplying paint cost per gallon and total gallons
    return fPaintCostPerGalIn * iTotalGal # send total paint cost for usage

def getSalesTax(sStateIn): # find sales tax depending on state
    # Find sales tax percentage based on state entered
    match sStateIn:
        case "CT" | "VT":
            return .06
        case "MA":
            return .0625
        case "ME":
            return .085
        case "RI":
            return .07
        case _:
            return 0
    # send sales tax by state for usage

def showCostEstimate(iTotalGal, fLaborHr, fLaborCost, fPaintCost, fSalesTax, sLast):
    #Calculate total labor cost, total tax, and total cost
    fTotalLaborCost = fLaborCost * iTotalGal
    fTotalTax = fSalesTax * (fTotalLaborCost + fPaintCost)
    fTotalCost = fPaintCost + fTotalLaborCost + fTotalTax
    # Print out calculations
    print(f"Gallons of paint: {iTotalGal}")
    print(f"Hours of labor: {fLaborHr}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fTotalLaborCost:,.2f}")
    print(f"Tax: ${fTotalTax:,.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

    # write to file! initialize, open, then write
    sFileName = f"{sLast}_PaintJobOutput.txt"
    with open(sFileName, 'w') as f:
        f.write(f"Gallons of paint: {iTotalGal}")
        f.write(f"Hours of labor: {fLaborHr}")
        f.write(f"Paint charges: ${fPaintCost:,.2f}")
        f.write(f"Labor charges: ${fTotalLaborCost:,.2f}")
        f.write(f"Tax: ${fTotalTax:,.2f}")
        f.write(f"Total cost: ${fTotalCost:,.2f}")
    # print out that file was created
    print(f"File: {sFileName} was created.")

def main():
    # Prompt for input and convert into float
    fWallSqFt = getFloatInput("Enter wall space in square feet: ")
    fPricePerGal = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGal = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGal = getFloatInput("How many labor hours per gallon: ")
    fLaborPerHour = getFloatInput("Labor charge per hour: ")
    # Prompt for which state job is in to find sales tax
    sState = input("State job is in: ").upper()
    # Prompt for customers last name
    sLastName = input("Customer last name: ").title()

# Call functions for calculations

    # Call function to find how many gallons, total labor hours, total labor charges, total paint cost, sales tax
    iTotalGallons = getGallonsOfPaint(fWallSqFt, fFeetPerGal)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGal, iTotalGallons)
    fTotalLaborCost = getLaborCost(fLaborHoursPerGal, fLaborPerHour)
    fTotalPaintCost = getPaintCost(fPricePerGal, iTotalGallons)
    fSalesTax = getSalesTax(sState)

    # Call function to print out calculations and create file
    showCostEstimate(iTotalGallons, fTotalLaborHours, fTotalLaborCost, fTotalPaintCost,
                     fSalesTax, sLastName)

main()