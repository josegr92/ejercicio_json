#_*_ coding:utf-8 _*_

import json

fich=open("areas-recreativas.json","r")
doc=json.load(fich)
fich.close()

for directorio in doc["directorios"]["directorio"]:
	print "Nombre: %s"%directorio["nombre"]["content"]
	direccion=directorio["direccion"]
	print direccion[0]

print "\n"
print "Áreas recreativas con la categoria Miradores"
for directorio in doc["directorios"]["directorio"]:
	for categoria in directorio["categorias"]["categoria"]:
		if categoria["content"]=="Miradores":
			print directorio["nombre"]["content"]

print "\n"
cont=0
nom=raw_input("Introduce el nombre del área recreativa: ")
for directorio in doc["directorios"]["directorio"]:
	if directorio["nombre"]["content"]==nom:
		localizacion=directorio["localizacion"]["content"].split()
		latitud=localizacion[0]
		longitud=localizacion[1]
		print "http://www.openstreetmap.org/#map=14/%s/%s"%(latitud,longitud)
	cont=cont+1

print "\n"
print "Hay %i áreas recreativas"%cont

print "\n"
print "Identificadores de las áreas recreativas"
for directorio in doc["directorios"]["directorio"]:
	print "Identificador: %s"%directorio["identificador"]

ident=int(raw_input("Introduce el identificador del área recreativa: "))
for directorio in doc["directorios"]["directorio"]:
	if directorio["identificador"]==ident:
		print "Nombre: %s"%directorio["nombre"]["content"]