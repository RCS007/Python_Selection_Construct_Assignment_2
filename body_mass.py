# Problem 2:
    
# Write a program that interprets body mass index.
# Body mass index (BMI) is a measure of health based on weight. It can be calculated by taking your weight in
# kilograms and dividing it by the square of your height in meters. The interpretation of BMI for people 16
# years and older is as follows:

# BMI | Interpretation
# _______________________________
# Below 18.5 | Underweight
# 18.5–24.9  | Normal
# 25.0–29.9  | Overweight
# Above 30.0 | Obese

# Write a program that prompts the user to enter a weight in Kilograms and height in inches and then
# displays the BMI. Note that and one inch is 0.0254 meters.

# Define conversion factor for inches to meters
INCH_TO_METER = 0.0254

# Get user input for weight in kilograms and height in inches
weight = float(input("Enter your weight in kilograms: "))
height_in_inches = float(input("Enter your height in inches: "))

# Convert height from inches to meters
height_in_meters = height_in_inches * INCH_TO_METER

# Calculate BMI
bmi = weight / (height_in_meters ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display the BMI and category
print(f"Your BMI is: {bmi:.2f}")
print(f"Interpretation: {category}")
