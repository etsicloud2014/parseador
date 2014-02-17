#!/usr/bin/python
from xml.dom import minidom
import os, time
import codecs


class gestion_plantilla(object):
	def __init__(self,nombre_fichero):
		self.nom_fich=nombre_fichero + ".xml"
		try:
			self.arbol_dom=minidom.parse(os.path.realpath(self.nom_fich))
			self.doc_root=self.arbol_dom.documentElement
		except:
			print "No se ha podido abrir el arcivo"
		#self.info_path='/home/borja/ecloud/parseador/ficheros_nuevos'
		self.info_path='./ficheros_nuevos'

	def mostrar_arbol_dom(self):
		print self.arbol_dom.toprettyxml()

	def modificar_atributo(self, atributo, texto):
		nodos=self.arbol_dom.childNodes
		lista = nodos[0].getElementsByTagName("nodos")
		for nodo in lista:
			x=nodo.getElementsByTagName(atributo)[0]
			x.childNodes[0].nodeValue = texto
	def guardar(self):
		#fichero=open(os.path.realpath(self.info_nombre_raw+"_parseado"+".xml"),"w")
		#fichero=self.info_nombre_raw+"_parseado"+".xml"
		fichero=codecs.open(self.info_nombre_raw+"_parseado"+".xml",'w','utf-8')
		self.arbol_dom.writexml(fichero, encoding='utf-8')
		fichero.close()
		
		
	def obtener_info(self):
		self.info_nombre=os.listdir(self.info_path)[0]
		self.info_nombre_raw, self.info_extension=os.path.splitext(self.info_nombre)
	def elegir_parseador(self):
		if self.info_extension != ".txt":
			print "Esta version del parseador no soporta este tipo de archivos"
			return 1
		else:
			print 'Tipo de extension valida'
			return 0
		
	def obtener_fecha(self):
		self.info_fecha=time.ctime(os.path.getmtime(self.info_path +'/'+ self.info_nombre))
	
	def obtener_texto(self):
		fichero=open(os.path.realpath(self.info_path +'/'+ self.info_nombre),"r")
		cadena=fichero.read()
		self.info_text=unicode(cadena,'utf-8')
		print self.info_text
		fichero.close()
	

		


plantilla=gestion_plantilla('plantilla')
#plantilla.mostrar_arbol_dom()
#plantilla.modificar_atributo('date',plantilla.info_fecha)
#plantilla.mostrar_arbol_dom()
#plantilla.guardar()
plantilla.obtener_info()
print plantilla.info_nombre
print plantilla.info_extension
print plantilla.info_nombre_raw
if plantilla.elegir_parseador() == 1:
	exit(1)
plantilla.obtener_fecha()
print plantilla.info_fecha
plantilla.obtener_texto()
plantilla.modificar_atributo('title',plantilla.info_nombre_raw)
plantilla.modificar_atributo('date',plantilla.info_fecha)
plantilla.modificar_atributo('text',plantilla.info_text)
plantilla.mostrar_arbol_dom()
plantilla.guardar()
