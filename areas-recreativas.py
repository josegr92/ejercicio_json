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