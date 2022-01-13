time = int(input("Пожалуйста, введите необходимое количество секунд: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Конвертация времени в формате чч:мм:сс - {hours}:{minutes}:{seconds}")