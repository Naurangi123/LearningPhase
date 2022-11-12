def bodymassindex(height,weight):
    return round((weight/height**2),2)

h=float(input("Enter your height in meters:"))
w=float(input("Enter ypiur weight in kg:"))

print("Welcome to the BMI Calculater.")

bmi=bodymassindex(h,w)
print("Your bmi is:",bmi)

if bmi<=17.8:
    print("You are underweight.")
elif 17.8< bmi<=25.9:
    print("Your weight is normal.")
elif 25.9<bmi<=31.5:
    print("You are overweight.")
else:
    print("You are very Weak.")