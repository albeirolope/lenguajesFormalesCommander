from comandos import *


#MENU DE OPCIONES
print("¡Hola!, querido usuario, a continuación creara los alfabetos con los cuales realizaré sus requerimientos, recuerde que como minimo debe ingresar 2 alfabetos, GRACIAS. ")
C=0 #creamos un contador
while C<2:
        
    objectAlfabeto=Alfabetos()
    C=C+1
    if C>=2:
        OpAl=0
        while OpAl==0:
            OpAl=int(input("¿Deseas ingresar otro alfabeto? Digite 1 para Si, 2 para NO? "))
            if(OpAl==1):
                C=1
            elif(OpAl==2):
                print("Elegiste no crear mas alfabetos")    
            else:
                print("Ingrese una opcion valida")
                OpAl=0    

            
objectAlfabeto.mostrarAlfabetos()
alfabetos=objectAlfabeto.getAlfabetos()

Op=1
while Op != 6: #Se ejecuta mientras op sea diferente de 4
   

    print('1.Realizar Union De Alfabetos\n2.Realizar La Diferencia Entre Alfabetos\n3.Realizar La Interseccion Entre Alfabetos\n4.Calcular La Cerradura De Estrella\n5. Crear lenguajes ---> \n6.Salir ') #Muestra las opciones
    Op = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion
    
    if Op == 1:
        c=True
        while c:
            n=int(input("Digite cuantos alfabetos desea unir : \n"))
            if(n>len(objectAlfabeto.getAlfabetos())):
                print("No tiene esa cantidad de alfabetos creados, digite una cantidad válida")
            else:
                print( unionAlfabetos(n,alfabetos).ejecutar())
                c=False    
        
    elif Op == 2:
        n1=int(input("Digita el numero del alfabeto que desea hacer la diferecia: \n"))-1
        n2=int(input("Digita el numero del otro alfabeto : \n"))-1
        print(diferenciaDeConjuntos(alfabetos[n1],alfabetos[n2]).ejecutar())
    elif Op == 3:
        n1=int(input("Digita el numero del alfabeto: \n"))-1
        n2=int(input("Digita el numero del otro alfabeto: \n"))-1
        print(interseccionDeConjuntos(alfabetos[n1],alfabetos[n2]).ejecutar())
    elif Op == 4:
        n=int(input("Digite la cantidad maxima de palabras que desea generar con el alfabeto: \n"))
        iAlfabeto=int(input("Digite el numero del alfabeto con el cual desea realizar la cerradura de estrella: \n"))-1
        print(cerraduraDeEstrella(alfabetos[iAlfabeto],n).ejecutar())    
    elif Op == 5:
        i=0
        print("     Hola querido usuario, a continuacion crearas lenguajes aleatorios en base a los alfabetos que creaste anteriormente")
        validacion=True
        while validacion:
            nLenguajes=int(input("      ¿Cuantos lenguajes deseas crear?, recuerda que como minimo deben ser 2 lenguajes: \n"))
            if nLenguajes<2:
                print("     Como minimo debes crear 2 lenguajes")
            else:
                validacion=False
        while i<nLenguajes:
            
            
            n=int(input("       ¿Cuantas palabras desea crear para este lenguaje?: \n"))
            val=True
            while val:
                indiceDeAlfabeto=int(input("        Digite el numero del alfabeto con el que generará el lenguaje: \n"))
                if indiceDeAlfabeto>len(alfabetos):
                    print("     No tiene esa cantidad de alfabetos")
                else:
                    val=False
            objectLenguaje=Lenguajes(alfabetos[indiceDeAlfabeto-1],n)
            i=i+1
            
            

            
        print("     ------------- SUB MENU DE LENGUAJES -------------")  
        objectLenguaje.mostarLenguaje()
        lenguajes=objectLenguaje.getLenguaje()
        opsubmenu=0
        while opsubmenu!=8:
            print("     1.Calcular union entre lenguajes \n     2.Calcular diferencia entre lenguajes \n     3.Calcular la intersección entre lenguajes\n     4.Calcular la concatenación entre lenguajes\n     5.Calcular la potencia de un lenguaje\n     6.Calcular la inversa de un lenguaje\n     7.Calcular la cardinalidad de un lenguaje \n     8.Salir")  

            opsubmenu=int(input("     Elija una opcion: \n"))

            if opsubmenu==1:
                c=True
                while c:
                    n=int(input("     Digite cuantos lenguajes desea unir : \n"))
                    if(n>len(lenguajes)):
                        print("     No tiene esa cantidad de lenguajes creados, digite una cantidad válida")
                    else:
                        print(unionLenguajes(n,lenguajes).ejecutar())
                        c=False  
            elif opsubmenu==2:
                i1=int(input("     Ingrese el numero del primer lenguaje: \n"))-1
                i2=int(input("     Ingrese el numero del segundo lenguaje: \n"))-1
                print(diferenciaDeConjuntos(lenguajes[i1],lenguajes[i2]).ejecutar())
            elif opsubmenu==3:
                n1=int(input("     Digita el numero del lenguaje:  \n"))-1
                n2=int(input("     Digita el numero del otro lenguaje:  \n"))-1
                print(interseccionDeConjuntos(lenguajes[n1],lenguajes[n2]).ejecutar())
            elif opsubmenu==4:
                n1=int(input("     Digita el numero del lenguaje: \n"))-1
                n2=int(input("     Digita el numero del otro lenguaje: \n"))-1
                print(concatenacionDeLenguajes(lenguajes[n1],lenguajes[n2]).ejecutar())
            elif opsubmenu==5:
                n1=int(input("     Ingrese el numero del lenguaje:  \n "))-1
                n=int(input("     Digite la potencia:  \n"))
                print(potenciaDeUnLenguaje(lenguajes[n1],n).ejecutar())
            elif opsubmenu==6:
                n1=int(input("     Ingrese el numero del lenguaje:  \n "))-1
                print(inversaDeunLenguaje(lenguajes[n1]).ejecutar())
            elif opsubmenu==7:
                n1=int(input("     Ingrese el numero del lenguaje: \n"))-1
                print("     La cardinalidad del lenguaje numero ",n1+1," es: ", len(lenguajes[n1]))
            elif opsubmenu==8:
                pass
    elif Op == 6:
        s= True     
