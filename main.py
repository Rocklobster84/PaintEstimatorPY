# Stephanie Thompson 
# Paint Calculator
import math

gallonsNeeded = 0.0
cansNeeded = 0.0
sqftPerGallon = 350.0
gallonsPerCan = 1.0

# Create var and Prompt for wall height input
wallHeight = input("Enter wall height (feet): ")

# Create var Prompt for wall width input
wallWidth = input("Enter wall width (feet): ")

# Calculate and output wall area
wallArea = wallHeight * wallWidth
print(wallArea)

# Calculate and output number of gallons needed