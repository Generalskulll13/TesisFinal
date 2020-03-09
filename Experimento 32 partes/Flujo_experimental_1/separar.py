# -*- coding: utf-8 -*-
import random
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from time import time
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

archivo=open("LLNcooperativa.txt",'r')
noticias=open("noticias1.txt",'w')
topico=open("topicos.txt",'r')
partes1=open("partes1.txt",'w')
topicos1=open("topicos1.txt",'w')
partes2=open("partes2.txt",'w')
topicos2=open("topicos2.txt",'w')
partes3=open("partes3.txt",'w')
topicos3=open("topicos3.txt",'w')
partes4=open("partes4.txt",'w')
topicos4=open("topicos4.txt",'w')
partes5=open("partes5.txt",'w')
topicos5=open("topicos5.txt",'w')
partes6=open("partes6.txt",'w')
topicos6=open("topicos6.txt",'w')
partes7=open("partes7.txt",'w')
topicos7=open("topicos7.txt",'w')
partes8=open("partes8.txt",'w')
topicos8=open("topicos8.txt",'w')
partes9=open("partes9.txt",'w')
topicos9=open("topicos9.txt",'w')
partes10=open("partes10.txt",'w')
topicos10=open("topicos10.txt",'w')
partes11=open("partes11.txt",'w')
topicos11=open("topicos11.txt",'w')
partes12=open("partes12.txt",'w')
topicos12=open("topicos12.txt",'w')
partes13=open("partes13.txt",'w')
topicos13=open("topicos13.txt",'w')
partes14=open("partes14.txt",'w')
topicos14=open("topicos14.txt",'w')
partes15=open("partes15.txt",'w')
topicos15=open("topicos15.txt",'w')
partes16=open("partes16.txt",'w')
topicos16=open("topicos16.txt",'w')
partes17=open("partes17.txt",'w')
topicos17=open("topicos17.txt",'w')
partes18=open("partes18.txt",'w')
topicos18=open("topicos18.txt",'w')
partes19=open("partes19.txt",'w')
topicos19=open("topicos19.txt",'w')
partes20=open("partes20.txt",'w')
topicos20=open("topicos20.txt",'w')
partes21=open("partes21.txt",'w')
topicos21=open("topicos21.txt",'w')
partes22=open("partes22.txt",'w')
topicos22=open("topicos22.txt",'w')
partes23=open("partes23.txt",'w')
topicos23=open("topicos23.txt",'w')
partes24=open("partes24.txt",'w')
topicos24=open("topicos24.txt",'w')
partes25=open("partes25.txt",'w')
topicos25=open("topicos25.txt",'w')
partes26=open("partes26.txt",'w')
topicos26=open("topicos26.txt",'w')
partes27=open("partes27.txt",'w')
topicos27=open("topicos27.txt",'w')
partes28=open("partes28.txt",'w')
topicos28=open("topicos28.txt",'w')
partes29=open("partes29.txt",'w')
topicos29=open("topicos29.txt",'w')
partes30=open("partes30.txt",'w')
topicos30=open("topicos30.txt",'w')
partes31=open("partes31.txt",'w')
topicos31=open("topicos31.txt",'w')
partes32=open("partes32.txt",'w')
topicos32=open("topicos32.txt",'w')
archivospartes=[]
archivostopicos=[]
archivospartes.append(partes32)
archivospartes.append(partes31)
archivospartes.append(partes30)
archivospartes.append(partes29)
archivospartes.append(partes28)
archivospartes.append(partes27)
archivospartes.append(partes26)
archivospartes.append(partes25)
archivospartes.append(partes24)
archivospartes.append(partes23)
archivospartes.append(partes22)
archivospartes.append(partes21)
archivospartes.append(partes20)
archivospartes.append(partes19)
archivospartes.append(partes18)
archivospartes.append(partes17)
archivospartes.append(partes16)
archivospartes.append(partes15)
archivospartes.append(partes14)
archivospartes.append(partes13)
archivospartes.append(partes12)
archivospartes.append(partes11)
archivospartes.append(partes10)
archivospartes.append(partes9)
archivospartes.append(partes8)
archivospartes.append(partes7)
archivospartes.append(partes6)
archivospartes.append(partes5)
archivospartes.append(partes4)
archivospartes.append(partes3)
archivospartes.append(partes2)
archivospartes.append(partes1)
archivostopicos.append(topicos32)
archivostopicos.append(topicos31)
archivostopicos.append(topicos30)
archivostopicos.append(topicos29)
archivostopicos.append(topicos28)
archivostopicos.append(topicos27)
archivostopicos.append(topicos26)
archivostopicos.append(topicos25)
archivostopicos.append(topicos24)
archivostopicos.append(topicos23)
archivostopicos.append(topicos22)
archivostopicos.append(topicos21)
archivostopicos.append(topicos20)
archivostopicos.append(topicos19)
archivostopicos.append(topicos18)
archivostopicos.append(topicos17)
archivostopicos.append(topicos16)
archivostopicos.append(topicos15)
archivostopicos.append(topicos14)
archivostopicos.append(topicos13)
archivostopicos.append(topicos12)
archivostopicos.append(topicos11)
archivostopicos.append(topicos10)
archivostopicos.append(topicos9)
archivostopicos.append(topicos8)
archivostopicos.append(topicos7)
archivostopicos.append(topicos6)
archivostopicos.append(topicos5)
archivostopicos.append(topicos4)
archivostopicos.append(topicos3)
archivostopicos.append(topicos2)
archivostopicos.append(topicos1)
nacional=[]
mundo=[]
entretencion=[]
otro=[]
numero=0
top=[]
noticias=[]
for notic in archivo.readlines():
	noticias.append(notic)
for linea in topico.readlines():
	aux=int(linea)
	top.append(aux)
	if aux==0 :
		nacional.append(numero)
	if aux==1 :
		mundo.append(numero)
	if aux==2 :
		entretencion.append(numero)
	if aux==3 :
		otro.append(numero)
	numero=numero+1
print (len(nacional))
print (len(mundo))
print (len(entretencion))
print (len(otro))
n=0
print (len(noticias))
while n<31 :
	random.seed(3)
	muestra1=random.sample(nacional,144)
	for letra in muestra1:
		nacional.remove(letra)
	random.seed(3)
	muestra2=random.sample(mundo,42)
	for letra in muestra2:
		mundo.remove(letra)
	random.seed(3)
	muestra3=random.sample(entretencion,33)
	for letra in muestra3:
		entretencion.remove(letra)
	random.seed(3)
	muestra4=random.sample(otro,16)
	for letra in muestra4:
		otro.remove(letra)
	muestra1=muestra1+muestra2+muestra3+muestra4
	muestra1.sort()
	for num in muestra1:
		archivospartes[n].write(str(noticias[num]))
		archivostopicos[n].write(str(top[num]))
		archivostopicos[n].write('\n')
	n=n+1
muestra1=nacional+mundo+entretencion+otro
muestra1.sort()
for num in muestra1:
	archivospartes[n].write(str(noticias[num]))
	archivostopicos[n].write(str(top[num]))
	archivostopicos[n].write('\n')
print (len(nacional))
print (len(mundo))
print (len(entretencion))
print (len(otro))



