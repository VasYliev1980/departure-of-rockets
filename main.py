def CheckRentList(rentList):
    rent_end = -1
    for rent in sorted(rentList, key=lambda item: item[0]):  # сортируем расписания по времени начала
        if rent[0] < rent_end:  # проверяем что время старта текущего расписания больше времени окончания предыдущего
            return False
        rent_end = rent[1]

    return True


rentList = [
    (1, 3), (7, 9), (4, 6), (8, 15), (17, 20), (20, 23)
]

print(CheckRentList(rentList))