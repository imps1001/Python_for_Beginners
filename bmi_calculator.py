def calculate_bmi(height, weight):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_calculator():
    print("Welcome to the BMI Calculator!")

    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {category}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")

if __name__ == "__main__":
    bmi_calculator()
