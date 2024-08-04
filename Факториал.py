from math import factorial
try:
    number = int(input('Введите целое положительное число '))
    
    if number >0:
        print('Факториал введенного числа равен',factorial(number))
    else:
        print('Число не может быть меньше или равным нулю')

except ValueError as e:
    print(f"Ошибка: {e}. Пожалуйста, введите положительное целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")