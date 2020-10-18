def sum_weights(weight_1, weight_2):
  return(weight_1 + weight_2)

def calc_avg_weight(weight_1, weight_2):
  temp = sum_weights(weight_1, weight_2)
  return(temp / 2)

def run():
  beepWeight = int(input("What is the weight of Beep?"))
  bopWeight = int(input("What is the weight of Bop?"))
  calcType = input("What would you like to calculate? (sum or average)")

  if (calcType.lower() == "sum"):
    print("The sum of Beep and Bop's weight is {}".format(sum_weights(beepWeight, bopWeight)))
  elif (calcType.lower() == "average"):
    print("The average of Beep and Bop's weight is {}".format(calc_avg_weight(beepWeight, bopWeight)))
  else:
    print("Calculation type invalid.")
  
run()