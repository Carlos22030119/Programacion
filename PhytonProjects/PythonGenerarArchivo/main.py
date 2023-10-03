import random
import datetime
import time

def Hora():
    horaactual = datetime.datetime.now()
    auxiliar = ""+str(horaactual.hour).zfill(2)+":"+str(horaactual.minute).zfill(2)+":"+str(horaactual.second).zfill(2)
    return auxiliar

id = 1
titulos = "ID_TRABAJO|HORA_LLEGADA|TIEMPO_CPU|PRIORIDAD\n"
proyeMin = 20
proyeMax = 100
prioriMin = 1
prioriMax = 5
sleepMin = 1
sleepMax = 2
proceMin = 1
proceMax = 4
procesa = random.randint(proceMin,proceMax)
proye = random.randint(proyeMin,proyeMax)
proyectos = []
proyectos.append(titulos)
for n in range(proye):
    aux = " "+str(id).zfill(2)+"|"
    aux = aux + str(Hora())+"|"
    priori = random.randint(prioriMin,prioriMax)
    sleep = random.randint(sleepMin,sleepMax)
    aux = aux + str(procesa).zfill(2)+"|"+str(priori).zfill(2)+"\n"
    id = id+1
    #print(aux)
    proyectos.append(aux)
    time.sleep(sleep)
with open("archivo.dat","w") as archivo:
    for n in proyectos:
        archivo.write(n)
archivo.close()    