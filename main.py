def shto_nadet(temperatura, est_osadki, silnye_osadki):

    if 20 < temperatura < 30:
        if est_osadki:
            return "Футболку, шорты и дождевик"
        else:
            return "Футболку и шорты"


    elif temperatura > 0:
        if est_osadki:
            if silnye_osadki:
                return "Пальто, резиновые сапоги и зонт"
            else:
                return "Пальто и дождевик"
        else:
            return "Пальто"


    else:
        return "Пуховик"



temperatura = float(input("Введите температуру: "))


if 20 < temperatura < 30:

    est_osadki = input("Есть осадки? (да/нет): ") == "да"

    result = shto_nadet(temperatura, est_osadki, False)
else:

    if temperatura > 0:

        est_osadki = input("Есть осадки? (да/нет): ") == "да"
        if est_osadki:

            silnye_osadki = input("Осадки сильные? (да/нет): ") == "да"

            result = shto_nadet(temperatura, est_osadki, silnye_osadki)
        else:

            result = shto_nadet(temperatura, False, False)
    else:

        result = shto_nadet(temperatura, False, False)


print(f"Рекомендация: {result}")