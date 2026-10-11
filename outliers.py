# outliers.py

numbers = [10, 12, 11, 13, 100, 12, 11]

threshold = 50

print("Original numbers:", numbers)
print("Outliers:")

for number in numbers:
    if number > threshold:
        print(number)
