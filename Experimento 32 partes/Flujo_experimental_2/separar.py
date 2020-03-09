# -*- coding: utf-8 -*-
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
nacional=[]
mundo=[]
entretencion
otro=[]
numero=1
for linea in topico.readlines():
	aux=int(linea)
	if aux==0 :
		nacional.append(numero)
	if aux==1 :
		mundo.append(numero)
		if aux==2 :
		entretencion.append(numero)
	if aux==3 :
		otro.append(numero)
	numero=numero+1
print len(nacional)
print len(mundo)
print len(entretencion)
print len(otro)