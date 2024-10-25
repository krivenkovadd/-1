numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_numbers = numbers[:4] + numbers[5:]
# TODO заменить значение пропущенного элемента средним арифметическим
average = sum(new_numbers) / len(numbers)
list_numbers = numbers[:4] + [average] + numbers[5:]
print("Измененный список:", list_numbers)
