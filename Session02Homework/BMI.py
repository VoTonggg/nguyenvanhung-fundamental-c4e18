height_cm = int(input("Input your height in cm: "))
weight_kg = int(input("Input your weight: "))

height_m = height_cm / 100

bmi_index = weight_kg / (height_m * height_m)

if bmi_index < 16:
    print("Severely underweight")
elif bmi_index < 18.5:
    print("Underweight")
elif bmi_index < 25:
    print("Normal")
elif bmi_index < 30:
    print("Overweight")
else:
    print("Obese")

