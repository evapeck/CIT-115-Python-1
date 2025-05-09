# Author: Eva Peck
# Date: 2/21/2025
# Inter Planetary Weights: Calculate weight differences on each planet


# Named Constants

MERCURY_GRAV = 0.38
VENUS_GRAV = 0.91
MOON_GRAV = 0.165
MARS_GRAV = 0.38
JUPITER_GRAV = 2.34
SATURN_GRAV = 0.93
URANUS_GRAV = 0.92
NEPTUNE_GRAV = 1.12
PLUTO_GRAV = 0.066

# User Input

sName = input("What is your name? ")
fEarthWeight = float(input("What is your weight? "))

# Calculate Planetary Weights

fMercuryWeight = fEarthWeight * MERCURY_GRAV
fVenusWeight = fEarthWeight * VENUS_GRAV
fMoonWeight = fEarthWeight * MOON_GRAV
fMarsWeight = fEarthWeight * MARS_GRAV
fJupiterWeight = fEarthWeight * JUPITER_GRAV
fSaturnWeight = fEarthWeight * SATURN_GRAV
fUranusWeight = fEarthWeight * URANUS_GRAV
fNeptuneWeight = fEarthWeight * NEPTUNE_GRAV
fPlutoWeight = fEarthWeight * PLUTO_GRAV

# Output Planetary Weights

print("\nHere are your weights on our Solar System's planets, " + sName + "\n")

print(format("Weight on Mercury: ", '25') + format(fMercuryWeight,'10.2f'))
print(format("Weight on Venus: ", '25') + format(fVenusWeight,'10.2f'))
print(format("Weight on our Moon: ", '25') + format(fMoonWeight,'10.2f'))
print(format("Weight on Mars: ", '25') + format(fMarsWeight,'10.2f'))
print(format("Weight on Jupiter: ", '25') + format(fJupiterWeight,'10.2f'))
print(format("Weight on Saturn: ", '25') + format(fSaturnWeight,'10.2f'))
print(format("Weight on Uranus: ", '25') + format(fUranusWeight,'10.2f'))
print(format("Weight on Neptune: ", '25') + format(fNeptuneWeight,'10.2f'))
print(format("Weight on Pluto: ", '25') + format(fPlutoWeight,'10.2f'))

