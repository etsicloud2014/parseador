#!/usr/bin/python
from xml.dom import minidom
import xml.etree.cElementTree as ET


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
	nodos=arbol_dom.childNodes
	nodo=nodos[0].getElementsByTagName("title")[0]
	nodo.nodeValue="adios"
	print arbol_dom.toxml()

def pruebaNodos():
	arc_xml=minidom.parse('plantilla.xml')
	nodos=arc_xml.childNodes
	print "Acceso directo a nodos:"
	print nodos[0].toxml()
def VisualizarNodos (lista, nivel):
	for nodo in lista:
		nodo.text="adios"
		print("   ")*nivel, nodo.nodeName, nodo.nodeValue
		VisualizarNodos (nodo.childNodes, nivel + 1)
def prueba2xml():
	root = ET.Element("root")

	doc = ET.SubElement(root, "doc")

	field1 = ET.SubElement(doc, "field1")
	field1.set("name", "blah")
	field1.text = "some value1"

	field2 = ET.SubElement(doc, "field2")
	field2.set("name", "asdfasd")
	field2.text = "some vlaue2"

	tree = ET.ElementTree(root)
	tree.write("filename.xml")

print "hola mundo"
#creartxt()
#grabartxt()
#leertxt()
pruebaxml()
#pruebaNodos()
#arc_xml=minidom.parse('plantilla.xml')
#VisualizarNodos(arc_xml.childNodes,0)
#prueba2xml()
