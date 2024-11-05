# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main program
def main():
    print("Welcome to the BMI Calculator!")
    
    # Input validation for weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(e)

    # Input validation for height
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            break
        except ValueError as e:
            print(e)

    # Calculate BMI and categorize
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    # Display result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

# Run the program
main()