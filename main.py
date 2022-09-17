
import AFN_to_AFD_transformer
import regextransformer


#Menú


jelly = 0

while jelly == 0:
    print("\n-------Escoga una de las opciones para continuar-------")
    print("1. Transformación de expresión regular a postfix\n2. Generación de AFN (Archivo)\n3. Conversión AFN a AFD (Archivo)\n4. Generación de AFD Directo (Archivo)\n5. Minimización de AFD’s (Archivo)\n6. Simulación AFN y AFD\n7. Salir del programa")

    try:
        opcion = int(input())
        if opcion == 1:
            print("Transformación de expresión regular a postfix")
            regextransformer()
        elif opcion == 2:
            print("Generación de AFN (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("AFN.txt",'w')
        elif opcion == 3:
            print("Conversión AFN a AFD (Archivo)\nSe creará un archivo txt del resultado.")
            AFN_to_AFD_transformer()
        elif opcion == 4:
            print("Generación de AFD Directo (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("AFDD.txt",'w')
        elif opcion == 5:
            print("Minimización de AFD’s (Archivo)\nSe creará un archivo txt del resultado.")
            f=open("minimizado.txt",'w')
        elif opcion == 6:
            print("Simulación AFN y AFD\nSe creará un archivo txt del resultado.")
        elif opcion == 7:
            jelly=1
            print("Programa cerrado")
        else:
            print("Escoga una de las opciones ingresando solamente el número")
    except:
        print("Debe escoger una opción valida")



