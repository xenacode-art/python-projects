while True:
 weight_kg =float(input("Enter weight in kg: ")) 
 weight_lbs = weight_kg / 0.45 
 weight="Your weight in pound is: {:.2f} Lbs\n\n".format(weight_lbs) 
 print(weight)