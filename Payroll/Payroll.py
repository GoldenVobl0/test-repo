# -*- coding: utf-8 -*-

print("Расчет ЗП")
print("--------------------------------")

print("Коэффициенты по сумме: ")
print("Минимальный - 0.6")
print("Выше минимального - 0.85")
print("Средний - 0.95")
print("Выше среднего - 1")
print("Высокий - 1.1")
print("Максимальный - 1.2")
print("--------------------------------")

print("Коэффициенты по новым подключениям: ")
print("От 0 до 2 - 0.7")
print("От 3 до 4 - 0.9")
print("Ровно 5 - 1")
print("От 6 до 10 - 1.03")
print("От 11 до 21 - 1.05")
print("От 22 до 43 - 1.07")
print("От 44 - 1.09")
print("--------------------------------")

print("Коэффициенты по модулям: ")
print("От 0 до 3 - 0.8")
print("От 4 до 6 - 0.9")
print("От 7 до 9 - 1")
print("От 10 до 12 - 1.03")
print("От 13 до 15 - 1.07")
print("От 16 - 1.1")
print("--------------------------------")

print("Показатели продаж: ")
sum_all = int(input("Общая сумма проплат: "))
kkt_tov = int(input("Cумма товаров АСЦ: "))
ofd = int(input("Cумма товаров ОФД: "))
kkt_usl = int(input("Cумма услуг по ККТ: "))
moduls = int(input("Сумма модулей: "))
kol_ed = int(input("Количество новых подключений: "))
kol_mod = int(input("Количество модулей: "))
fine_sum = int(input("Сумма штрафа: "))
conf_ed = 0
conf_plan = 0
conf_mod = 0
print("--------------------------------")

sum_vuch = kkt_tov + ofd + kkt_usl + moduls
print("Сумма вычета из плана -", sum_vuch)
sum_ras = sum_all - sum_vuch
sum_ras_fine = sum_ras - fine_sum
print("Сумма чистых оплат -", sum_ras)
print("--------------------------------")

if kol_ed == 0 or kol_ed <= 2:
    conf_ed = 0.7
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed >= 3 and kol_ed <= 4:
    conf_ed = 0.9
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed == 5:
    conf_ed = 1
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed >= 6 and kol_ed <= 10:
    conf_ed = 1.03
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed >= 11 and kol_ed <= 21:
    conf_ed = 1.05
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed >= 22 and kol_ed <= 43:
    conf_ed = 1.07
    print("Коэффициент по новым подключениям -", conf_ed)
elif kol_ed >= 44:
    conf_ed = 1.09
    print("Коэффициент по новым подключениям -", conf_ed)
else:
    print("Ошибка ввода")

if sum_ras < 75000:
    conf_plan = 0
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 75000 and sum_ras < 125000:
    conf_plan = 0.6
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 125000 and sum_ras < 225000:
    conf_plan = 0.85
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 225000 and sum_ras < 250000:
    conf_plan = 0.95
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 250000 and sum_ras < 350000:
    conf_plan = 1
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 350000 and sum_ras < 400000:
    conf_plan = 1.1
    print("Коэффициент по сумме -", conf_plan)
elif sum_ras >= 400000:
    conf_plan = 1.2
    print("Коэффициент по сумме -", conf_plan)
else:
    print("Ошибка ввода")

if kol_mod == 0 or kol_mod <= 3:
    conf_mod = 0.8
    print("Коэффициент по модулям -", conf_mod)
elif kol_mod >= 4 and kol_mod <= 6:
    conf_mod = 0.9
    print("Коэффициент по модулям -", conf_mod)
elif kol_mod >= 7 and kol_mod <= 9:
    conf_mod = 1
    print("Коэффициент по модулям -", conf_mod)
elif kol_mod >= 10 and kol_mod <= 12:
    conf_mod = 1.03
    print("Коэффициент по модулям -", conf_mod)
elif kol_mod >= 13 and kol_mod <= 15:
    conf_mod = 1.07
    print("Коэффициент по модулям -", conf_mod)
elif kol_mod >= 16:
    conf_mod = 1.1
    print("Коэффициент по модулям -", conf_mod)
else:
    print("Ошибка ввода")
print("--------------------------------")

proc_asc = kkt_usl * 0.1
proc_ofd = ofd * 0.1
proc_mod = moduls * 0.15
ras = sum_ras_fine * 0.38 * 0.25 * conf_mod * conf_plan * conf_ed
sum_zp = ras + proc_asc + proc_ofd + proc_mod + 2400
print("Сумма ЗП - %.2f" % sum_zp)
print("--------------------------------")
input("Выход")