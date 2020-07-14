import math
def cash_to_coins(dollars):
  dollars = int(dollars * 100)
  coins = {
    "pennies" : 0,
    "nickels" : 0,
    "dimes" : 0,
    "quarters": 0
  }
  remainder = dollars % 25
  coins["quarters"] = int((dollars - remainder) / 25)
  dollars = remainder
  remainder = dollars % 10
  coins["dimes"] = int((dollars - remainder) / 10)
  dollars = remainder
  remainder = dollars % 5
  coins["nickels"] = int((dollars - remainder) / 5)
  dollars = remainder
  remainder = dollars % 1
  coins["pennies"] = int((dollars - remainder) / 1)

  print(remainder)

  print(coins)

cash_to_coins(8.69)