weight_input = float(input("Weight: "))
weight_type = input("Kg or Lbs? ")

if weight_type.lower() == "kg":
    converted = str(weight_input * 2.20462)
    print(f"{converted[0:5]}lbs")
elif weight_type.lower() == "lbs":
    converted = str(weight_input * 0.453592)
    print(f"{converted[0:5]}kg")
else:
    print("bonak dalawa lang choices abnoy ka ba?")
