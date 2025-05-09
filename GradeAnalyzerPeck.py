# CIT-115
# Grade Analyzer
# Eva Peck
# 4/12/25

#Input User Name
sName = input("Name of person that we are calculating the grades for:  ")

#Test Score Input
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

# Drop or Not
sDrop = input("Do you want to drop the lowest grade? Y or N: ")

# Validate entries > 0
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Decision Structure
# User wants to drop the lowest Test score
if sDrop == "Y" or sDrop == "y":
    fDivideBy = 3.0
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        iLowestGrade = iTest1
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        iLowestGrade = iTest2
    elif iTest3 <= iTest4:
        iLowestGrade = iTest3
    else:
        iLowestGrade = iTest4

# User does not want to drop the lowest test score
elif sDrop == "N" or sDrop == "n":
    fDivideBy = 4.0
    iLowestGrade = 0

# User did not enter Y or N
else:
    print("Enter Y or N to drop the lowest grade")
    exit()

# Calculate average using logic
fTestAverage = ((iTest1 + iTest2 + iTest3 + iTest4) - iLowestGrade) / fDivideBy

# Find letter grade
if fTestAverage >= 97.0:
    sLetterGrade = "A+"
elif fTestAverage >= 94.0:
    sLetterGrade = "A"
elif fTestAverage >= 90.0:
    sLetterGrade = "A-"
elif fTestAverage >= 87.0:
    sLetterGrade = "B+"
elif fTestAverage >= 84.0:
    sLetterGrade = "B"
elif fTestAverage >= 80.0:
    sLetterGrade = "B-"
elif fTestAverage >= 77.0:
    sLetterGrade = "C+"
elif fTestAverage >= 74.0:
    sLetterGrade = "C"
elif fTestAverage >= 70.0:
    sLetterGrade = "C-"
elif fTestAverage >= 67.0:
    sLetterGrade = "D+"
elif fTestAverage >= 64.0:
    sLetterGrade = "D"
elif fTestAverage >= 60.0:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F"

# Print Test Average and Letter Grade
print(f"{sName}'s test average: {fTestAverage:.1f}")
print(f"Letter Grade: {sLetterGrade}")
                    
                
        
