import random

mix = random.sample(range(1,76),75)

production = []

for i in range(75):
  input("エンターを選択してください")
  number = mix[i]
  production.append(number)


  print(f"今回の出玉: {number}")
  print(f"今までの出玉: {production}")


print(f"すべての出玉: {mix}")