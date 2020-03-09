# -*- coding: utf-8 -*-
import nltk.data
import re, string, unicodedata
import nltk
import spacy
from time import time
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import SnowballStemmer

def construye_diccionario(file):
	diccionario=[]
	for lineas in file.readlines():
		linea=lineas.split()
		linea[0]=linea[0].replace('_',' ')
		linea[0]=linea[0].replace('\n','')
		linea[1]=linea[1].replace('_',' ')
		linea[1]=linea[1].replace('\n',' ')
		diccionario.append(linea)
	return diccionario


def tokenize(text,diccionario):
	texto2=text
	words = nltk.word_tokenize(texto2)
	return words
def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        new_word=new_word.replace('_','')
        if new_word != '':
            new_words.append(new_word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('spanish'):
            new_words.append(word)  
    return new_words
def identificar_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word in stopwords.words('spanish'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    spanishStemmer=SnowballStemmer("spanish", ignore_stopwords=True)
    stems = []
    for word in words:
        stem = spanishStemmer.stem(word)
        stems.append(stem)
    return stems
def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    
    return words
def ngram(words,n):
	output = list(ngrams(words, n))
	return output
inicio=time()
archivo=open("flujo_estandar/partes1.txt",'r')
archivo6=open('flujo_estandar/dataset.csv','w')
archivo8=open("flujo_estandar/diccionarioespañol.txt",'r')

listadenoticias = []
listadengrmas=[]
diccionarios=construye_diccionario(archivo8)
numero=0
for linea in archivo.readlines():
	lineas= tokenize(linea,diccionarios)
	salida2=identificar_stopwords(lineas)
	lineas= normalize(lineas)
	lineas = remove_stopwords(lineas)
	#lineas= lemmatize_words(lineas,archivo1)
	lineas= stem_words(lineas)
	listadenoticias.append(lineas)
	numero=numero+1
for notici in listadenoticias:
	for palabras in notici:
		listadengrmas.append(palabras)
lista_nueva = []
ngramas=[]
for bigrama in listadengrmas:
	if bigrama not in ngramas:
		ngramas.append(bigrama)
topico=open("flujo_estandar/topicos1.txt",'r')
topicos=[]
for linea in topico.readlines():
	topicos.append(linea)
contador=0;
cuentalinea=1
for noticia in listadenoticias:
	archivo6.write(str(cuentalinea))
	archivo6.write(',')
	for ngr in ngramas:
		if ngr in noticia:
			archivo6.write('1,')
		else:
			archivo6.write('0,')
	archivo6.write(topicos[contador])
	cuentalinea=cuentalinea+1
	contador=contador+1
archivo.close()
archivo6.close()