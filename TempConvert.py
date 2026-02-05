#TempConvert.py
#Name:Louis Safranek
#Date:02/05/2026
#Assignment:Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = int(input("Give a Temperature in Farenheit"))
  tempC= round((tempF-32)*5/9,2)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
