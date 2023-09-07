import math

numbers = []
for i in range(10):
    while True:
      try:
        num = float(input(f"Введіть число під номером {i+1}-e: "))
        if num >= 0:
            numbers.append(num)
            break
        else:
            print("Це число не є додатнім")
      except ValueError:
        print("Ви ввели не число")
print(numbers)
print("Максимальний елемент списку", max(numbers))
if max(numbers) % 2 == 0:
    print("Число є парним")
else:
    print("Це число не парне")
print("Мінімальний елемент списку", min(numbers))
if min(numbers) % 2 == 0:
    print("Число є парним")
else:
    print("Це число не парне")
print("Середнє арифметичне цього списку: ", sum(numbers) / len(numbers))
c = max(numbers)
d = min(numbers)
print(math.gcd(int(c), int(d)))
