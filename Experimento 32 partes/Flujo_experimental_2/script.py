# -*- coding: utf-8 -*-
import os
from time import time
import re, string, unicodedata
archivo1=open("tiempos.txt",'w')
tiempo_inicial=time()
os.system( "python3 flujo_estandar/flujo_basico.py")
tiempo_final=time()
archivo1.write("tiempo del flujo estandar: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo estandar")
os.system( "python3 flujo_estandar/entropiamaxima.py")

print("termine de analisar el flujo estandar")
tiempo_inicial=time()
os.system( "python3 Flujo_experimental_1/flujo_basico1.py")
tiempo_final=time()
archivo1.write("tiempo del Flujo_experimental_1: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo experimental 1")
#os.system( "python3 Flujo_experimental_1/entropiamaxima.py")
print("termine de analisar el flujo experimental 1")
tiempo_inicial=time()
#os.system( "python3 Flujo_experimental_2/flujo_experimental2.py")
tiempo_final=time()
archivo1.write("tiempo del Flujo_experimental_2: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo experimental 2")
#os.system( "python3 Flujo_experimental_2/entropiamaxima.py")
print("termine de analisar el flujo experimental 2")
tiempo_inicial=time()
#os.system( "python3 Flujo_experimental_3/flujo_experimental3.py")
tiempo_final=time()
archivo1.write("tiempo del flujo_experimental3: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo experimental 3")
#os.system( "python3 Flujo_experimental_3/entropiamaxima.py")
print("termine de analisar el flujo experimental 3")
tiempo_inicial=time()
#os.system( "python3 flujo_estandar/flujo_basico.py")
tiempo_final=time()
archivo1.write("tiempo del flujo estandar: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo estandar")
#os.system( "python3 flujo_estandar/entropiamaxima.py")

print("termine de analisar el flujo estandar")
tiempo_inicial=time()
#os.system( "python3 Trigrama1/flujo_basico1.py")
tiempo_final=time()
archivo1.write("tiempo del Trigrama1: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo Trigrama1 1")
#os.system( "python3 Trigrama1/entropiamaxima.py")
print("termine de analisar el flujo Trigrama1 1")
tiempo_inicial=time()
#os.system( "python3 Trigrama2/flujo_experimental2.py")
tiempo_final=time()
archivo1.write("tiempo del Trigrama2: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo Trigrama2 2")
#os.system( "python3 Trigrama2/entropiamaxima.py")
print("termine de analisar el flujo Trigrama2 2")
tiempo_inicial=time()
#os.system( "python3 Trigrama3/flujo_experimental3.py")
tiempo_final=time()
archivo1.write("tiempo del Trigrama3: ")
archivo1.write(str(tiempo_final-tiempo_inicial))
archivo1.write('\n')
print("termine de preprocesar el flujo Trigrama 3")
#os.system( "python3 Trigrama3/entropiamaxima.py")
print("termine de analisar el flujo experimental 3")
print("termine de hacer todo")
#os.system("python archivo2.py")
#os.system("python archivo1.py")
#result=commands.getoutput('/pruebas/python3 entropiamaxima.py')