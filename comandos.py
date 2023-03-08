import random

class Comando():
    def ejecutar(self)->None:
        pass

class Alfabetos():
    __alfabetos=[] #Esta es la lista que almacena todos los alfabetos
    def __init__(self):
        contador=0
        alfabeto=[]
        nCaracteres=int(input("Cuantos caracteres deseas ingresar?: \n"))
        while contador<nCaracteres:
            caracter=str(input("Digite un caracter para el alfabeto: \n"))
            alfabeto.append(caracter)
            contador=contador+1
        self.__alfabetos.append(alfabeto)#Aqui almacenamos la lista alfabeto en la lista principal alfabetos que contiene todos los alfabetos
        print("Gracias por haber creado tu alfabeto \n")

    def mostrarAlfabetos(self):
        print("--------------- Alfabetos ---------------")
        for i in range(len(self.__alfabetos)):
            print(i+1,".",self.__alfabetos[i])
        print("-----------------------------------------")   
    def getAlfabetos(self):
        return self.__alfabetos

class Lenguajes():
    __lenguajes=[] #esta es la lista que almacena los lenguajes
    def __init__(self,alfabeto,n):
        
        lenguaje=cerraduraDeEstrella(alfabeto,n).ejecutar()
        self.__lenguajes.append(lenguaje)

    def mostarLenguaje(self):
        print("----------------- Lenguajes ----------------")
        for i in range(len(self.__lenguajes)):
            print(i+1, ".",self.__lenguajes[i])
        print("----------------------------------------------") 
    def getLenguaje(self):
        return self.__lenguajes






 

class unionAlfabetos(Comando):
    def __init__(self,n,objetoAlfabetos) :
        self.__n=n
        self.__objetoAlfabetos=objetoAlfabetos
    def ejecutar(self)->None:
        unido=[]
        c=0
        while c<self.__n:
            indice=int(input("Digite el numero del alfabeto que desea unir: \n"))-1
            unido=unido+self.__objetoAlfabetos[indice]
            c=c+1
        return set(unido)
class unionLenguajes(Comando):
    def __init__(self,n,lenguajes) :
        self.__n=n
        self.__lenguajes=lenguajes
    def ejecutar(self)-> None:
        unido=[]
        c=0
        while c<self.__n:
            indice=int(input("Digite el numero del lenguaje que desea unir: \n"))-1
            unido=unido+self.__lenguajes[indice]
            c=c+1
        return set(unido)
class diferenciaDeConjuntos(Comando):
    def __init__(self,n1,n2) :
        self.__n1=n1
        self.__n2=n2
    def ejecutar(self):
        diferencia=set(self.__n1).difference(self.__n2)
        return diferencia

class interseccionDeConjuntos(Comando):
    def __init__(self,n1,n2) :
        self.__n1=n1
        self.__n2=n2
    def ejecutar(self):
        intersec=set(self.__n1)&set(self.__n2)   
        return intersec    

class cerraduraDeEstrella(Comando):
    def __init__(self,alfabeto,n) -> None:
        self.__alfabeto=alfabeto
        self.__n=n
    def ejecutar(self):
        palabras=[]
        while len(palabras)<self.__n:
            palabra=''
            for i in range(random.randint(1,len(self.__alfabeto))):
                palabra=palabra+random.choice(self.__alfabeto)
            palabras.append(palabra)
        return palabras

class concatenacionDeLenguajes(Comando):
    def __init__(self,l1,l2) -> None:
        self.__l1=l1
        self.__l2=l2
    def ejecutar(self):
        concatenacionLenguaje=[]
        for i in range(len(self.__l1)):
            for j in range(len(self.__l2)):
                concatenacionLenguaje.append(self.__l1[i]+self.__l2[j])

        return concatenacionLenguaje


class potenciaDeUnLenguaje(Comando):
    def __init__(self,l1,n):
        self.__l1=l1
        self.__n=n
    def ejecutar(self): #usamos recursividad para la potencia
        temp=self.__l1
        for i in range(self.__n-1):
            temp=temp+concatenacionDeLenguajes(self.__l1,temp).ejecutar()
            potenciaDeUnLenguaje(temp,self.__n-1)
        return set(temp)

class inversaDeunLenguaje(Comando):
    def __init__(self,l) -> None:
        self.__l=l
    def ejecutar(self) -> None:
        lenguaje=self.__l
        for i in range(len(lenguaje)):
            lenguaje[i]=''.join(reversed(lenguaje[i]))
        return lenguaje    
            


    