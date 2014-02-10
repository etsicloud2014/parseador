#!/usr/bin/python

from xml.dom import minidom
import os


class gestion_plantilla(object):
	def __init__(self,nombre_fichero):
		self.nom_fich=nombre_fichero + ".xml"
		try:
			self.arbol_dom=minidom.parse(os.path.realpath(self.nom_fich))
			self.doc_root=self.arbol_dom.documentElement
		except:
			print "No se ha podido abrir el arcivo"

	def mostrar_arbol_dom(self):
		print self.arbol_dom.toprettyxml()

	def modificar_atributo(self, atributo, texto):
		nodos=self.arbol_dom.childNodes
		lista = nodos[0].getElementsByTagName("nodos")
		for nodo in lista:
			print "hola"
			x=nodo.getElementsByTagName("title")[0]
			x.childNodes[0].nodeValue = "adios"
			print x.nodeValue
			#nodo.nodeValue="adios"
	def guardar(self):
		fichero=open(os.path.realpath("nuevo_fichero"),"w")
		self.arbol_dom.writexml(fichero, encoding='iso-8859-1')
		fichero.close()

		


plantilla=gestion_plantilla('plantilla')
plantilla.mostrar_arbol_dom()
plantilla.modificar_atributo('title','adios')
plantilla.mostrar_arbol_dom()
plantilla.guardar()
