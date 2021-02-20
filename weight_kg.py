while True:
  weight_lbs =float(input("Enter weight in pounds: "))
  weight_kg = weight_lbs * 0.45
  weight="Your weight in kg is: {:.2f}KG  \n\n" .format(weight_kg)
  print(weight)