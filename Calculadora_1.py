import math

while True:
    print("""
    CALCULADORA PROYECTOS A.I.I
    
    1) Suma
    2) Resta
    3) Multiplicacion
    4) División
    5) Potencia 
    6) Raíz Cuadrada
    7) Apagar
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        try:
         n1 = float(input("Introduce tu primer número: ") )
         n2 = float(input("Introduce tu segundo número: ") )
         print(" ")
         print("RESULTADO:",n1+n2)
        except :
            print("solo puede ingresar numeros")

             
    elif opcion == 2:
          try:
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           print(" ")
           print("RESULTADO:",n1-n2)
          except :
              print("solo puede ingresar numeros")

           
    elif opcion == 3:
          try:
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           print(" ")
           print("RESULTADO:",n1*n2)
          except :
              print("solo puede ingresar numeros")
          

    elif opcion == 4:
          try:
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           print(" ")
           print("RESULTADO:",n1/n2)
          except ZeroDivisionError:
              print("el segundo numero no puede ser 0")
          except:
              print("solo puede ingresar numeros")

    elif opcion == 5:
        try:
         n1 = float(input("Introduce el numero que sera la base: ") )
         n2 = float(input("Introduce el numero que sera la potencia: ") )
         print(" ")
         print("RESULTADO:",n1**n2)
        except :
            print("solo puede ingresar numeros")

    elif opcion == 6:
          try:
           n1 = float(input("Introduce un número: ") )
           print(" ")
           print("RESULTADO:",math.sqrt(n1))
          except:
              print("solo puede ingresar un numero")

    elif opcion == 7:
        break
    else:
        print("Opción incorrecta")