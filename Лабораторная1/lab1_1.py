numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
none_position = numbers.index(None)
numbers[none_position] = 0
''' 0 не влияет на среднее арифметическое в данном случае.
     Если использовать срезы, то кол-во элементов всё-равно учитывает None'''
avrg = (sum(numbers)) / len(numbers)
numbers[none_position] = avrg
print("Измененный список:", numbers)

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

 # Способ со срезами:

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_position = numbers.index(None)
avrg = sum(numbers[0:none_position]) + sum(numbers[none_position + 1:])/len(numbers)
numbers[none_position] = avrg
print(f"Измененный список: {numbers}")