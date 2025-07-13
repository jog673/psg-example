tiempo_segundos= 788521 
tiempo_dias= tiempo_segundos/(60*60*24)
tiempo_horas=(tiempo_dias-round(tiempo_dias))*24
tiempo_minutos=(tiempo_horas-round(tiempo_horas))*60
tiempo_segundos=round((tiempo_minutos-round(tiempo_minutos))*60)
print(f"{round(tiempo_dias)} días {round(tiempo_horas)} horas {round(tiempo_minutos)} minutos {round(tiempo_segundos)} segundos")