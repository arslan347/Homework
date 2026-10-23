temperature = float(input("Введите вашу температуру: "))

pressure = int(input("Введите ваше давление: "))

pulse = int(input("Введите ваш пульс: "))

#проверка серьезности ситуации
if (temperature < 35 or temperature > 38 or
        pressure < 105 or pressure > 140 or
        pulse < 55 or pulse > 110):
    
  print("Требуется врач")

#проверка на нормальное состояние
elif 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    
  print("Нормальное состояние")

#проверка на небольшое отклоение от нормы
else:
    
  print("Легкое недомогание")
