def main():
    print("Welcome to BMI Calculator")
    
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        bmi = weight /(height ** 2)
        category = get_bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {category}")
    except ValueError:
        print("Invalid input, please enter numberic  values.")
    
def get_bmi_category(bmi):
    if  bmi < 18.5:
        return "Underweight"
    elif 18.5 <=bmi <25:
        return  "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ ==  "__main__":
   main()