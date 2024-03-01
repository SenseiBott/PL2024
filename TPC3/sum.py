import re

def calculateSum(inputText):
  values = re.findall(r"(on|off|=|\d+)", inputText, flags=re.I)
  totalSum = 0
  state = True

  for value in values:
    if value.lower() == "on":
      state = True
    elif value.lower() == "off":
      state = False
    elif value == "=":
      print("Sum =", totalSum)
    else:
      if state:
        totalSum += int(value)

with open("test.txt", "r") as file:
  inputText = file.read()
calculateSum(inputText)
