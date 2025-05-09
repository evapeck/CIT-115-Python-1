# Author: Eva Peck
# Date: 3/5/25
# Purpose: Temperature Converter


#Input temperature and Fahrenheit or Celsius

print("Eva Peck's Temp Converter: \n \n")
fTemp = float(input("Enter a temperature: "))
sDegree = input("Is the temp F for Fahrenheit or C for Celsius? ")

# Equivalent Decision Structure

    # Fahrenheit to Celsius Conversion
if sDegree == "F" or sDegree == "f" and fTemp < 212:
    fCelsiusEquiv = (5.0/9.0) * (fTemp - 32)
    fRoundedCelsiusEquiv = round(fCelsiusEquiv, 1)
    print(f"The Celsius equivalent is: {fRoundedCelsiusEquiv}")

    # Celsius to Fahrenheit Conversion
elif sDegree == "C" or sDegree == "c" and fTemp < 100:
    fFahrenheitEquiv = ((9.0/5.0) * fTemp) + 32
    fRoundedFahrenheitEquiv = round(fFahrenheitEquiv, 1)
    print(f"The Fahrenheit equivalent is: {fRoundedFahrenheitEquiv}")
    
    # Fahrenheit Temp too high
elif sDegree == "F" or sDegree == "f" and fTemp > 212:
    print("Temp can not be > 212")
    
    # Celsius Temp too high
elif sDegree == "C" or sDegree == "c" and fTemp > 100:
    print("Temp can not be > 100")

    # User did not enter F or C
else:
    print("Enter a F or C")
    
        


