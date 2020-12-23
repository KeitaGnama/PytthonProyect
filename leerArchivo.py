from os import write


def crearArchivo():
    archivo=open('datos.txt','w')
    archivo.close()

    #escribir en el archivo
def escribirArchivo():
    archivo=open('datos.txt','w')
    archivo.write('keita gnama\n')
    archivo.write('4448436187')
    archivo.close

def leerArchivo():
    archivo=open('datos.txt','r')
    linea=archivo.readline()    
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()
leerArchivo()