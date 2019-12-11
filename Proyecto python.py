#Juan Mora Fortis, Sergi Eduard Vila Sanchez, Robert Xavier Vila Sanchez#
#Proyecto Python#
#Juego Conecta 4 o 4 en raya#

class jugador:
    def __init__(self):
        self.nombre=""
        self.marca=""

    def atributosJugador(self,string):
        self.nombre=input(string)
        self.marca=input("Escoge una marca para el juego: ")

def pedirCoordenada(string):
    a=input(string)
    try:
        a=int(a)
        if (a>6 or a<1):
            print("No existe esa casilla.")
            return pedir(string)
        return a
    
    except ValueError:
        print("Debes introducir un numero, prueba de nuevo.")
        return pedir(string)
    
class  Tabla:
    def __init__(self):
        self.tabla=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],
                    [" "," "," "," "," "," "],[" "," "," "," "," "," "],
                    [" "," "," "," "," "," "],[" "," "," "," "," "," "]]
        self.final=False
        self.ganador_Juego=""
        self.Turno_Juego=""
        
    def dibujarTablero(self):
        #j referencia a la fila y c a la columna
        i=0
        while (i<12):
            if (i%2==0):
                j=int(i/2)
                for c in range(6):
                    print("|" ,self.tabla[j][c]," ",end="")
                print("|")
            if (i%2!=0):
                print("-----"*6)
            i+=1
        print("   1    2    3    4    5    6   ") #Numero de columna

    def ejecutarJugada(self,jugador):
        string="Es el turno de: "+jugador.nombre+". Escoge la posicion donde colocar tu ficha"
        c=pedirCoordenada(string)
        j=5 
        correcto= False

        while not correcto:
            if (self.tabla[0][c-1]!=" "):
                print("Columna llena.")
                c=pedirCoordenada(string)
            elif(self.tabla[j][c-1]==" "):
                self.tabla[j][c-1]=jugador.marca
                correcto= True
            else:
                j -= 1#La ficha rellena el espacio mas abajo vacio de las columnas
        import os
        os.system('cls')
        self.dibujarTablero()
    def ganarPartida(self,jugador):
        j=5
        #Comprobacion en horizontal
        while j>=0 and self.final==False:
            #comparar la fila j columna 2-5
            if jugador.marca==self.tabla[j][5] and self.tabla[j][5]==self.tabla[j][4] and self.tabla[j][4]==self.tabla[j][3] and self.tabla[j][3]==self.tabla[j][2]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            #comparar fila j columna 1-4
            elif jugador.marca==self.tabla[j][4] and self.tabla[j][4]==self.tabla[j][3]and self.tabla[j][3]==self.tabla[j][2] and self.tabla[j][2]==self.tabla[j][1]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            #comparar fila j columna 0-3
            elif jugador.marca==self.tabla[j][3] and self.tabla[j][3]==self.tabla[j][2] and self.tabla[j][2]==self.tabla[j][1] and self.tabla[j][1]==self.tabla[j][0]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            j-=1
            
        c=0
        #Comprobacion en vertical
        while c<=5 and self.final==False:
            #comparar la columna c filas 2-5
            if jugador.marca==self.tabla[5][c] and self.tabla[5][c]==self.tabla[4][c] and self.tabla[4][c]==self.tabla[3][c] and self.tabla[3][c]==self.tabla[2][c]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            #comparar la columna c filas 1-4
            elif jugador.marca==self.tabla[4][c] and self.tabla[4][c]==self.tabla[3][c] and self.tabla[3][c]==self.tabla[2][c] and self.tabla[2][c]==self.tabla[1][c]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            #comparar la columna c filas 0-3
            elif jugador.marca==self.tabla[3][c] and self.tabla[3][c]==self.tabla[2][c] and self.tabla[2][c]==self.tabla[1][c] and self.tabla[1][c]==self.tabla[0][c]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            c+=1

        #Comprobacion diagonal derecha a izquierda
        f=5
        while f>=3 and self.final == False:
            if jugador.marca==self.tabla[f][5] and self.tabla[f][5]==self.tabla[f-1][4] and self.tabla[f-1][4]==self.tabla[f-2][3] and self.tabla[f-2][3]==self.tabla[f-3][2]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            elif jugador.marca==self.tabla[f][4] and self.tabla[f][4]==self.tabla[f-1][3] and self.tabla[f-1][3]==self.tabla[f-2][2] and self.tabla[f-2][2]==self.tabla[f-3][1]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            elif jugador.marca==self.tabla[f][3] and self.tabla[f][3]==self.tabla[f-1][2] and self.tabla[f-1][2]==self.tabla[f-2][1] and self.tabla[f-2][1]==self.tabla[f-3][0]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            f-=1

        #Comprobacion diagonal izquierda a derecha
        f=5
        while f>=3 and self.final==False:
            if jugador.marca==self.tabla[f][0] and self.tabla[f][0]==self.tabla[f-1][1] and self.tabla[f-1][1]==self.tabla[f-2][2] and self.tabla[f-2][2]==self.tabla[f-3][3]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            elif jugador.marca==self.tabla[f][1] and self.tabla[f][1]==self.tabla[f-1][2] and self.tabla[f-1][2]==self.tabla[f-2][3] and self.tabla[f-2][3]==self.tabla[f-3][4]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            elif jugador.marca==self.tabla[f][2] and self.tabla[f][2]==self.tabla[f-1][3] and self.tabla[f-1][3]==self.tabla[f-2][4] and self.tabla[f-2][4]==self.tabla[f-3][5]:
                self.final=True
                self.ganador_Juego="Ha ganado: "+jugador.nombre
                print(self.ganador_Juego)
            f-=1
            
    def casoEmpate(self):
        if self.tabla[0][0]!=" " and self.tabla[0][1]!=" " and self.tabla[0][3]!=" " and self.tabla[0][4]!=" " and self.tabla[0][5]!=" ":
           self.final=True
           self.ganador_Juego="Empate"
           print(self.ganador_Juego)
           
    def jugarPartida(self,jugador1,jugador2):
        import random
        self.dibujarTablero()
        i=random.randint(1,2)
        while self.final==False:
            if (i%2==0):
                self.ejecutarJugada(jugador1)#Jugador elige donde colorcar su ficha
                self.ganarPartida(jugador1)#El programa comprueba si ha ganado
            elif(i%2!=0):
                self.ejecutarJugada(jugador2)
                self.ganarPartida(jugador2)
            i+=1
            self.casoEmpate()#Comprueba si el tablero esta lleno

#Programa principal (menu y esas cosas)
print("Bienvenido a nuestro 4 en raya cutre.")
print("Las instrucciones son simples, debes conectar 4 fichas verticalmente, horizontalmente y diagonalmente.\n"
      "Para ello deberas tener en cuenta que cuando selecciones una columna la ficha se colocara en la parte\n"
      "mas baja posible, gana el primero que cree una raya de 4 antes que el otro, SUERTE")
#Creamos jugador 1
jugador1=jugador()
jugador1.atributosJugador("Jugador 1, indicame tu nombre: ")
#Creamos jugador 2
jugador2=jugador()
jugador2.atributosJugador("Jugador 2, indicame tu nombre: ")

#Empezamos la partida
tabla=Tabla()
tabla.jugarPartida(jugador1,jugador2)

iniciado=True
while iniciado:
    tabla=Tabla()
    reiniciar = input("ﾂｿQuerﾃｩis jugar otra vez?(si/no)")
    if reiniciar == "si":
        pregunta=input("ﾂｿVais a jugar los mismos de antes?(si/no): ")
        while pregunta!="si" and pregunta!="no":
            pregunta=input("ﾂｿVais a jugar los mismos de antes?(si/no): ")
        if pregunta=="si":
            print("Juegan los mismos jugadores de antes, iniciando partida.")
        elif pregunta=="no":
            jugador1.atributosJugador("Jugador 1, indicame tu nombre: ")
            jugador2.atributosJugador("Jugador 2, indicame tu nombre: ")
        tabla.jugarPartida(jugador1,jugador2)
    elif reiniciar=="no":
        print("ﾂ｡Gracias por jugar!ﾂ｡Hasta la proxima!")
        iniciado=False
    




            
