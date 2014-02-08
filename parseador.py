#!/usr/bin/python
from xml.dom import minidom

def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.close()

def leertxt():
    archi=open('plantilla.xml','r')
    linea=archi.readline()
    while linea!="":
        print linea
        linea=archi.readline()
    archi.close()
def pruebaxml():
	arbol_dom=minidom.parse('plantilla.xml')
	print arbol_dom.toxml()

def pruebaNodos():
	arc_xml=minidom.parse('plantilla.xml')
	nodos=arc_xml.childNodes
	print "Acceso directo a nodos:"
	print nodos[0].toxml()
def VisualizarNodos (lista, nivel):
	for nodo in lista:
		print("   ")*nivel, nodo.nodeName, nodo.nodeValue
		VisualizarNodos (nodo.childNodes, nivel + 1)


print "hola mundo"
creartxt()
grabartxt()
leertxt()
pruebaxml()
pruebaNodos()
arc_xml=minidom.parse('plantilla.xml')
VisualizarNodos(arc_xml.childNodes,0)
