import datetime
import csv
import time

cadenaAux=[]
peatones=[]
peatonesH=[]
ciclistas=[]
ciclistasH=[]
autos=[]
autosH=[]
completado=[]

horaInicial=datetime.datetime(2023,10,17,21,30,0)

with open('C:\\Users\\verde\\OneDrive\\Documentos\\GitHub\\Programacion\\PhytonProjects\\GeneracionSemaforo\\archivoPetaon.dat','r') as archivo:
    for linea in archivo:
        cadenaAux= linea.split("|")
        peatonesH.append(cadenaAux[1])


while True:

    with open('C:\\Users\\verde\\OneDrive\\Documentos\\GitHub\\Programacion\\PhytonProjects\\GeneracionSemaforo\\archivoPetaon.dat','r') as archivo:
        i=0
        for linea in archivo:
            peatones.append(linea.strip())
            
         
            i=i+1#sirve para evaluar la cadenaH
        archivo.close

    horaInicial=horaInicial+datetime.timedelta(minutes=2)
    time.sleep(5)#cambiar a 120 en el programa final

    with open("C:\\Users\\sergi\\OneDrive\\Documentos\\GitHub\\Programacion\\PhytonProjects\\GeneracionSemaforo\\archivoCiclista.dat","r") as archivo:
        i=0
        for linea in archivo:
            ciclistas.append(linea.strip())
        
            i=i+1#sirve para evaluar la cadenaH
        archivo.close 
    
    with open("C:\\Users\\sergi\\OneDrive\\Documentos\\GitHub\\Programacion\\PhytonProjects\\GeneracionSemaforo\\archivoAuto.dat","r") as archivo:
        i=0
        for linea in archivo:
            autos.append(linea.strip())
        
            i=i+1#sirve para evaluar la cadenaH
        archivo.close 
   