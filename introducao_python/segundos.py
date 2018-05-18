entradaSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = entradaSegundos // (24 * 3600)
restoDias = entradaSegundos % (24 * 3600)
horas = restoDias // 3600
restoHoras = restoDias % 3600
minutos = restoHoras // 60
segundos = restoHoras % 60

print(dias, "dias,", horas,"horas,", minutos, "minutos e", segundos, "segundos.")
