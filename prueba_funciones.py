import random
import numpy as np
import string


lista = [str(x) for x in range(1,16)]
arreglo = np.array(lista).reshape(5,3)
datos_requeridos = ["NIF:      ", "Nombre:   ", "Edad:     "]

def rev_letras(revisar):
    for letra in revisar:
        if letra not in string.ascii_letters:
            return False
    return True

def rev_numeros(checkar):
    for numero in checkar:
        if numero not in string.digits:
            return False
    return True

def GrabarNif():
    global arreglo
    global Gr_NIF
    global nif_verificado
    print("***** Siga los pasos para Grabar NIF *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        Gr_NIF = input()
        if Gr_NIF[-4] == "-":
            nif, dv = Gr_NIF.split("-")
            ver_nif = rev_numeros(nif)
            if len(Gr_NIF) == 12 and ver_nif == True and len(dv) == 3:
                nif_verificado = Gr_NIF
                arreglo[0][0] = Gr_NIF
                break
            else:
                print("NIF no es valido intente nuevamente.\n")
        print("NIF no es valido intente nuevamente.\n")
    while True:
        print("Ingrese Nombre. Ejemplo: Jaime Vicencio")
        gr_nombre = input()
        rev_nombre = rev_letras(gr_nombre)
        if len(gr_nombre) >= 8:
            arreglo[0][1] = gr_nombre
            break
        else:
            print("Nombre no es vàlido.")
    while True:
        print("Ingrese Edad. Ejemplo: 42")
        try:
            gr_edad = int(input())
            if gr_edad >= 0:
                arreglo[0][2] = gr_edad
                print("Datos Ingresados correctamente.\n")
                break
            else:
                print("Nombre no es vàlido.")
                
        except:
            print("Edad no valida, vuelva a intentarlo")
            
 
    
def BuscarNif():
    print("***** Siga los pasos para Buscar NIF *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        bu_nif = input()
        if bu_nif == Gr_NIF:
            print("NIF verificado correctamente.\n")
            a,s,d,f,g = arreglo
            for requerido,dato in zip(datos_requeridos,a):
                        print(requerido,dato)
                        print()
            print(f"NIF: {bu_nif}, pertenece a la Union Europea")
            break
        else:
            print("NIF no es valido intente nuevamente.\n")

def ImprimirCert():
    print("***** Siga los pasos para Imprimir Certificados *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        impr_nif = input()
        a,s,d,f,g = arreglo
        fecha_nac = "12 de Enero 1972"
        estado_con = "Casado/a"
        miembro = "SI"
        if impr_nif == Gr_NIF:
            print("NIF verificado correctamente.\n")
            print("1.- Certificado de Nacimiento.\n2.- Certificado Estado Conyugal.\n3.- Certificado Estado Conyugal.\n4.- Salir.\n ")
            try:
                imprimir_op = int(input())
                if imprimir_op >= 1 and imprimir_op <= 4:
                    if imprimir_op == 1:
                        print("***** Certificado de Nacimiento *****")
                        print(f"Nombre:                {a[1]}")
                        print(f"NIF:                   {a[0]}")
                        print(f"Edad:                  {a[2]}")
                        print(f"Fecha Nacimiento:      {fecha_nac})")
                        break
                    if imprimir_op == 2:
                        print("***** Certificado Estado Conyugal *****")
                        print(f"Nombre:                {a[1]}")
                        print(f"NIF:                   {a[0]}")
                        print(f"Edad:                  {a[2]}")
                        print(f"Estado Conyugal:       {estado_con})")
                        break
                    if imprimir_op == 3:
                        print("***** Certificado Pertenencia Union Europea *****")
                        print(f"Nombre:                {a[1]}")
                        print(f"NIF:                   {a[0]}")
                        print(f"Edad:                  {a[2]}")
                        print(f"Miembro Union Europea: {miembro}")
                        break
                    if imprimir_op == 4:
                        break                        
            except:
                print("Opcion no Vàlida. Vuelva a intentarlo")
        else:
            print("nif no registrado.")            
    
def Salir():
    print("Realizado por Jaime Vicencio Rubilar. Adìos")
    return 
        
                

    


arreglo = [[str(0) for x in range(3)] for x in range(5)]