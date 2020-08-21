import json
def readJson():
        file = open('archivojson.json', )
        data = json.load(file)
        file.close()
        print(data)
        return data
dict = readJson()
print(type(dict))
for element in dict:
    print(element)


import pandas as pd
dat=pd.read_csv('archivo.csv',header=0)
print(dat)
print(type(dat))
print()
from xml.dom import minidom
doc = minidom.parse("archivoxml.xml")
datos = doc.getElementsByTagName("dato")
print(type(datos))
for dato in datos:
    sid = dato.getAttribute("id")
    nombre = dato.getElementsByTagName("nombre")[0]
    apellido = dato.getElementsByTagName("apellido")[0]
    edad = dato.getElementsByTagName("edad")[0]
    curso = dato.getElementsByTagName("curso")[0]
    print("id:%s " % sid)
    print("nombre:%s" % nombre.firstChild.data)
    print("apellido:%s" % apellido.firstChild.data)
    print("edad:%s" % edad.firstChild.data)
    print("curso:%s" % curso.firstChild.data)
