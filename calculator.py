def main():
  line = "="
  wine = "_"
  print(line*56, end="\n")
  print(" | [1] addition | [2] substraction | [3] multiply | [4] divide | ", end="\n")
  print(line*56, end="\n")

  equa = int(input("What equation do you want to execute? |> "))

  if equa == 1:
      add()
  elif equa == 2:
      sub()
  elif equa == 3:
      mult()
  elif equa == 4:
      div()
  else:
    print(wine*56)
    print("| ! Please, insert one of the operations", end="\n")
    main()

def add():
  line = "="
  x = float(input("What's the first value?"))
  y = float(input("What's the second value?"))
  answer = float(x) + float(y)
  print(line*56)
  print("The result is: ")
  print(answer)

def sub():
  line = "="
  x = float(input("What's the first value?"))
  y = float(input("What's the second value?"))
  answer = float(x) - float(y)
  print(line*56)
  print("The result is: ")
  print(answer)

def mult():
  line = "="
  x = float(input("What's the first value?"))
  y = float(input("What's the second value?"))
  answer = float(x) * float(y)
  print(line*56)
  print("The result is: ")
  print(answer)

def div():
  line = "="
  x = float(input("What's the first value?"))
  y = float(input("What's the second value?"))
  answer = float(x) // float(y)
  print(line*56)
  print("The result is: ")
  print(answer)

main()