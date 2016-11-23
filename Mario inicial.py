from tkinter import *
from tkinter import ttk






## Menu Inicial Mario ##

ventanaMenu = Tk()
ventanaMenu.title("Menu Inicial")
menu = Canvas(ventanaMenu, width=1000, height=650, bg="black")
ventanaMenu.config(bg="black")
mario1player = PhotoImage(file="Menu1player.png")
mario2player = PhotoImage(file="Menu2player.png")
dif1playereasy = PhotoImage(file="easy1player.png")
dif1playerem = PhotoImage(file="e-m1player.png")
dif1playermedium = PhotoImage(file="medium1player.png")
dif1playerhard = PhotoImage(file="hard1player.png")
dif1playerhardcore = PhotoImage(file="hardcore1player.png")
dif2playereasy = PhotoImage(file="easy2player.png")
dif2playerem = PhotoImage(file="e-m2player.png")
dif2playermedium = PhotoImage(file="medium2player.png")
dif2playerhard = PhotoImage(file="hard2player.png")
dif2playerhardcore = PhotoImage(file="hardcore2player.png")
nom1player = PhotoImage(file="nombre1player.png")
nom2player = PhotoImage(file="nombre2player.png")
fondo = PhotoImage(file="fondojuego.png")
marioizq = PhotoImage(file="marioizq.png")
marioder = PhotoImage(file="marioder.png")
mariosaltader = PhotoImage(file="mariosaltader.png")
mariosaltaizq = PhotoImage(file= "mariosaltaizq.png")
luigiizq = PhotoImage(file="luigiizq.png")
luigider = PhotoImage(file="luigider.png")
shellverdeder= PhotoImage(file="Shellverdeder.png")
shellverdeizq = PhotoImage(file="Shellverdeizq.png")
menu.focus_set()
estadojuego = 0 # Estado 0 - menu inicial # estado 1 - menu dificultad # estado 2 - menu nombres
men1 = menu.create_image(0,0,image=mario1player,anchor=NW)
players = 1


        
def mover_menu(event):
    global men1
    global mario1player
    global mario2player
    global players
    global estadojuego
    if event.char == 's' and estadojuego==0:
        menu.delete(men1)
        men1 = menu.create_image(0,0,image=mario2player,anchor=NW)
        players = 2

    elif event.char == 'w' and estadojuego == 0:
        menu.delete(men1)
        men1 =  menu.create_image(0,0,image=mario1player,anchor=NW)
        players = 1
    
    return players


def selectdif(event):
    print("llama a selectdif")
    global players
    global mover_menu
    global men1
    global dif1playereasy
    global estadojuego
    global botCargarJuego
    menu.delete(men1)
    estadojuego = estadojuego +1
    if estadojuego == 1:
        if players == 1:
            men1 = menu.create_image(0,0,image=dif1playereasy,anchor=NW)
            menu.bind('<d>', mover_dif)
            menu.bind('<a>', mover_dif)
            menu.bind('<Return>', tomar_nombres)
            print("players = ",players)
            
        elif players == 2:
            men1 = menu.create_image(0,0,image=dif2playereasy,anchor=NW)
            menu.bind('<d>', mover_dif)
            menu.bind('<a>', mover_dif)
            menu.bind('<Return>', tomar_nombres)
            print("players = ",players)

dificultad = 0

def mover_dif(event):
    global men1
    global dificultad
    global players
    global estadojuego
    global dif1playereasy
    global dif1playerem
    global dif1playermedium
    global dif1playerhard 
    global dif1playerhardcore
    
    
    if players == 1 and estadojuego == 1:
        if event.char == 'd' and dificultad == 0:
            dificultad = dificultad +1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playerem,anchor=NW)
            print(dificultad)
            return mover_dif
        elif event.char == 'd' and dificultad == 1:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playermedium,anchor=NW)
            return mover_dif
        elif event.char == 'd' and dificultad ==2:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playerhard,anchor=NW)
            return mover_dif
        elif event.char == 'd' and dificultad == 3:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playerhardcore,anchor=NW)
            return mover_dif
        elif event.char =='d' and dificultad == 4:
            dificultad = dificultad
        elif event.char == 'a' and dificultad == 4:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playerhard,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 3:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playermedium,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 2:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playerem,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 1:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif1playereasy,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 0:
            dificultad = dificultad
        

    elif players == 2 and estadojuego==1 :
        if event.char == 'd' and dificultad == 0:
            dificultad = dificultad +1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playerem,anchor=NW)
            print(dificultad)
            return mover_dif
        elif event.char == 'd' and dificultad == 1:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playermedium,anchor=NW)
            return mover_dif
        elif event.char == 'd' and dificultad ==2:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playerhard,anchor=NW)
            return mover_dif
        elif event.char == 'd' and dificultad == 3:
            dificultad +=1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playerhardcore,anchor=NW)
            return mover_dif
        elif event.char =='d' and dificultad == 4:
            dificultad = dificultad
        elif event.char == 'a' and dificultad == 4:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playerhard,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 3:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playermedium,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 2:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playerem,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 1:
            dificultad = dificultad -1
            menu.delete(men1)
            men1 = menu.create_image(0,0,image=dif2playereasy,anchor=NW)
            return mover_dif
        elif event.char == 'a' and dificultad == 0:
            dificultad = dificultad
        
        
        

    return dificultad

def tomar_nombres(event):
    global men1
    global dificutad
    global estadojuego
    global players
    estadojuego = estadojuego +1
    print("la dificultad es",dificultad)
    menu.delete(men1)
    variable_string = StringVar()
    variable_string2 = StringVar()
   
    if players == 1 and estadojuego == 2:
        men1 = menu.create_image(0,0,image=nom1player,anchor=NW)
        nom1 = Entry(menu, textvariable=variable_string)
        menu.create_window(500,352,window=nom1)
        menu.bind('a',nada)
        menu.bind('d',nada)
        menu.bind('<Return>', Crearjuego)
        
        
    elif players==2 and estadojuego ==2:
        men1 = menu.create_image(0,0,image=nom2player,anchor=NW)
        nom1 = Entry(menu, textvariable=variable_string)
        menu.create_window(500,352,window=nom1)
        nom2 = Entry(menu,textvariable=variable_string2)
        menu.create_window(500,397,window=nom2)
        menu.bind('a',nada)
        menu.bind('d',nada)
        menu.bind('<Return>', Crearjuego)
    



def nada(event):
        return 'break'
        
            
if estadojuego == 0:
    menu.bind('<s>', mover_menu)
    menu.bind('<w>', mover_menu)
    menu.bind('<Return>', selectdif) 
ventanaMenu.resizable(width=False, height=False)


    ## Juego ##

def Crearjuego(event):
        global JC, mario,luigi, juego, dificultad, players, vidasM, vidasL, d
        menu.bind('<Return>',nada)
        print ("llama a Crear Juego")
        juego = Toplevel()
        juego.config(bg='black')
        juego.title("MarioBros")
        juego.geometry("1000x650")
        juego.resizable(width=False, height=False)
        JC = Canvas(juego, width=1000, height=650, bg="black")
        JC.focus_set()
        JC.pack()
        mapa = JC.create_image(0,0,image=fondo,anchor=NW)
        if players == 1:
            mario = JC.create_image(140,513,image=marioder,anchor=NW)
            JC.bind_all('<KeyPress>',presionado)
            JC.bind('<KeyRelease>',liberado)
            
        elif players == 2:
            mario = JC.create_image(140,513,image=marioder,anchor=NW)
            luigi = JC.create_image(810,513,image=luigiizq,anchor=NW)
            JC.bind_all('<KeyPress>',presionado)
            JC.bind('<KeyRelease>',liberado)
        vidasM = 5
        vidasL = 5
        if dificultad == 0:
            d = 0
        elif dificultad == 1:
            d = 5
        elif dificultad == 2:
            d = 10
        elif dificultad == 3:
            d = 15
        elif dificultad == 4:
            d = 20
        print(d)
        aparicion_Shell2()
        aparicion_Shell()
        juego.mainloop()

botones ={'a': False,'w':False,'d':False,'j':False,'i':False,'l':False}

def presionado(event):
    
    global botones, players
    if players==1:
        movermario()
    elif players==2:
        movermario()
        moverluigi()
    boton = event.keysym
    movimiento = ['w','a','d','j','i','l']
    if (boton in movimiento):
        botones[boton]= True

def liberado(event):
    global botones
    if players==1:
        movermario()
    elif players==2:
        movermario()
        moverluigi()
    boton = event.keysym
    movimiento = ['w','a','d','j','i','l']
    if (boton in movimiento):
        botones[boton]= False
    
        
estadomario = "derecha"
estadoluigi = "izquierda"
#Funciones Mario y Luigi

def movermario():
        global mario,JC,cordmario,estadomario, botones, shell2, estadoshell2
        cordmario = JC.coords(mario)         
        if (botones['d']== True):
                JC.delete(mario)
                mario = JC.create_image(int(cordmario[0]),int(cordmario[1]),image=marioder,anchor=NW)
                JC.move(mario,10,0)
                print(int(cordmario[0]),int(cordmario[1]))
                estadomario = "derecha"
                if (cordmario[0]) > 960:
                        JC.coords(mario,5,int(JC.coords(mario)[1]))
                elif JC.coords(mario)[1] == 405 and (JC.coords(mario)[0] >= 330 and JC.coords(mario)[0] <= 620): ## Caida de la 1ra plat
                        caer()
                elif JC.coords(mario)[1] == 279 and (JC.coords(mario)[0] >= 227 and JC.coords(mario)[0] <= 281): ## Caida de la 1ra plat
                        caer()
                elif JC.coords(mario)[1] == 279 and (JC.coords(mario)[0] >= 662 and JC.coords(mario)[0] <= 722): ## Caida de la 1ra plat
                        caer()
                elif JC.coords(mario)[1] == 153 and (JC.coords(mario)[0] >= 326 and JC.coords(mario)[0] <= 616): ## Caida de la 1ra plat
                        caer()
                                    
                
        elif (botones['a']== True):
                JC.delete(mario)
                mario = JC.create_image(int(cordmario[0]),int(cordmario[1]),image=marioizq,anchor=NW)
                JC.move(mario,-10,0)
                estadomario = "izquierda"
                if (cordmario[0]) < -40:
                        JC.coords(mario,960,int(JC.coords(mario)[1]))
                elif JC.coords(mario)[1] == 405 and (JC.coords(mario)[0] >= 330 and JC.coords(mario)[0] <= 620): ## Caida de la 1ra plat
                        caer()
                elif JC.coords(mario)[1] == 279 and (JC.coords(mario)[0] >= 227 and JC.coords(mario)[0] <= 281): ## Caida de la 2da plat
                        caer()
                elif JC.coords(mario)[1] == 279 and (JC.coords(mario)[0] >= 662 and JC.coords(mario)[0] <= 722): ## Caida de la 2da plat
                        caer()
                elif JC.coords(mario)[1] == 153 and (JC.coords(mario)[0] >= 326 and JC.coords(mario)[0] <= 616): ## Caida de la 3ra plat
                        caer()
        elif (botones['w']== True) and limite==-1:
                saltar()
        
limite = -1

def moverluigi():
        global luigi,JC,cordluigi,estadoluigi
        cordluigi = JC.coords(luigi)
        
        if (botones['l']== True):
                JC.delete(luigi)
                luigi = JC.create_image(int(cordluigi[0]),int(cordluigi[1]),image=luigider,anchor=NW)
                JC.move(luigi,10,0)
                estadoluigi = "derecha"
                if (cordluigi[0]) > 960:
                        JC.coords(luigi,5,int(JC.coords(luigi)[1]))
                elif JC.coords(luigi)[1] == 405 and (JC.coords(luigi)[0] >= 330 and JC.coords(luigi)[0] <= 620): ## Caida de la 1ra plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 279 and (JC.coords(luigi)[0] >= 227 and JC.coords(luigi)[0] <= 281): ## Caida de la 1ra plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 279 and (JC.coords(luigi)[0] >= 662 and JC.coords(luigi)[0] <= 722): ## Caida de la 1ra plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 153 and (JC.coords(luigi)[0] >= 326 and JC.coords(luigi)[0] <= 616): ## Caida de la 1ra plat
                        caerluigi()
                
        elif (botones['j']== True):
                JC.delete(luigi)
                luigi = JC.create_image(int(cordluigi[0]),int(cordluigi[1]),image=luigiizq,anchor=NW)
                JC.move(luigi,-10,0)
                estadoluigi = "izquierda"
                if (cordluigi[0]) < -40:
                        JC.coords(luigi,960,int(JC.coords(luigi)[1]))
                elif JC.coords(luigi)[1] == 405 and (JC.coords(luigi)[0] >= 330 and JC.coords(luigi)[0] <= 620): ## Caida de la 1ra plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 279 and (JC.coords(luigi)[0] >= 227 and JC.coords(luigi)[0] <= 281): ## Caida de la 2da plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 279 and (JC.coords(luigi)[0] >= 662 and JC.coords(luigi)[0] <= 722): ## Caida de la 2da plat
                        caerluigi()
                elif JC.coords(luigi)[1] == 153 and (JC.coords(luigi)[0] >= 326 and JC.coords(luigi)[0] <= 616): ## Caida de la 3ra plat
                        caerluigi()
        elif (botones['i']== True) and limite==-1:
                saltarluigi()
       

limite = -1         


def saltar():
        print ("llama a saltar mario")
        global JC,mario,cordmario,juego,estadomario,limite, shell2, estadoshell2
        limite = 0
        if estadoshell2 == "creado":
            X1s2 = JC.coords(shell2)[0]
            X2s2 = (JC.coords(shell2)[0])+60
            Ys2 = JC.coords(shell2)[1]
            X2m = (JC.coords(mario)[0])+50
        if estadomario == "derecha":
            
            while limite <= 130:
                x = int(JC.coords(mario)[0])
                y = int(JC.coords(mario)[1])
                
                JC.delete(mario)
                mario = JC.create_image(x,y,image=mariosaltader,anchor =NW)
                JC.move(mario,1,-6)
                JC.update()
                ventanaMenu.after(10)
                if y-6 == 495 and not(x >= 330 and x < 620):
                    break
                elif y-6 == 369 and not (x >=229 and x < 736):
                    break
                elif y-6 == 369 and (x >=290 and x < 665):
                    break
                elif y-6 == 243 and not(x>330 and x<620):
                    break
                elif estadoshell2== "creado":
                    if (y-6 != 513 and Ys2 == 415) and (x <= X2s2 and X2m >=X1s2):
                        JC.delete(shell2)
                        estadoshell2 = "destruido"
                        break
                limite+=5
            limite=0
            while limite <= 130:
                x = int(JC.coords(mario)[0])
                y = int(JC.coords(mario)[1])
                JC.delete(mario)
                mario = JC.create_image(x,y,image=mariosaltader,anchor =NW)
                JC.move(mario,1,6)
                JC.update()
                ventanaMenu.after(10)
                if y+6 == 513 or (y+6 == 405 and not(x >= 330 and x < 620)) :
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioder,anchor=NW)
                    break
                elif y+6 == 279 and not(x>229 and x<736):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioder,anchor=NW)
                    break
                elif y+6 == 279 and(x>285 and x<670):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioder,anchor=NW)
                    break
                elif y+6 == 153 and not(x >= 330 and x < 620):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioder,anchor=NW)
                    break
                limite+=5
        elif estadomario == "izquierda":
            while limite <= 130:
                x = int(JC.coords(mario)[0])
                y = int(JC.coords(mario)[1])
                JC.delete(mario)
                mario = JC.create_image(x,y,image=mariosaltaizq,anchor =NW)
                JC.move(mario,-1,-6)
                JC.update()
                ventanaMenu.after(10)
                if y-6 == 495 and not(x >= 330 and x < 620):
                    break
                elif y-6 == 369 and not (x >=229 and x < 736):
                    break
                elif y-6 == 369 and (x >=290 and x < 665):
                    break
                elif y-6 == 243 and not(x>330 and x<620):
                    break
                elif estadoshell2== "creado":
                    if (y-6 != 495 and Ys2 == 415) and (x <= X2s2 and X2m >=X1s2):
                        JC.delete(shell2)
                        estadoshell2 = "destruido"
                        break
                    
                limite+=5
            limite=0
            while limite <= 130:
                x = int(JC.coords(mario)[0])
                y = int(JC.coords(mario)[1])
                JC.delete(mario)
                mario = JC.create_image(x,y,image=mariosaltaizq,anchor =NW)
                JC.move(mario,-1,6)
                JC.update()
                ventanaMenu.after(10)
                if y+6 == 513 or (y+6 == 405 and not(x >= 330 and x < 620)):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioizq,anchor=NW)
                    break
                elif y+6 == 279 and not(x>229 and x<736):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioizq,anchor=NW)
                    break
                elif y+6 == 279 and(x>285 and x<670):
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioizq,anchor=NW)
                    break
                elif y+6 == 153 and not(x >= 330 and x < 620) :
                    JC.delete(mario)
                    mario = JC.create_image(x,y+6,image=marioizq,anchor=NW)
                    break
                limite+=5
        limite=-1

def saltarluigi():
        global JC,luigi,cordluigi,juego,estadoluigi,limite
        limite = 0
        X1s2 = JC.coords(shell2)[0]
        X2s2 = (JC.coords(shell2)[0])+60
        Ys2 = JC.coords(shell2)[1]
        X2l = (JC.coords(luigi)[0])+50
        if estadoluigi == "derecha":
            while limite <= 130:
                x = int(JC.coords(luigi)[0])
                y = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(x,y,image=luigider,anchor =NW)
                JC.move(luigi,1,-6)
                JC.update()
                ventanaMenu.after(10)
                if y-6 == 495 and not(x >= 330 and x < 620):
                    break
                elif y-6 == 369 and not (x >=229 and x < 736):
                    break
                elif y-6 == 369 and (x >=290 and x < 665):
                    break
                elif y-6 == 243 and not(x>330 and x<620):
                    break
                
                limite+=5
            limite=0
            while limite <= 130:
                x = int(JC.coords(luigi)[0])
                y = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(x,y,image=luigider,anchor =NW)
                JC.move(luigi,1,6)
                JC.update()
                ventanaMenu.after(10)
                if y+6 == 513 or (y+6 == 405 and not(x >= 330 and x < 620)) :
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigider,anchor=NW)
                    break
                elif y+6 == 279 and not(x>229 and x<736):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigider,anchor=NW)
                    break
                elif y+6 == 279 and(x>285 and x<670):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigider,anchor=NW)
                    break
                elif y+6 == 153 and not(x >= 330 and x < 620):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigider,anchor=NW)
                    break
                limite+=5
        elif estadoluigi == "izquierda":
            while limite <= 130:
                x = int(JC.coords(luigi)[0])
                y = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(x,y,image=luigiizq,anchor =NW)
                JC.move(luigi,-1,-6)
                JC.update()
                ventanaMenu.after(10)
                if y-6 == 495 and not(x >= 330 and x < 620):
                    break
                elif y-6 == 369 and not (x >=229 and x < 736):
                    break
                elif y-6 == 369 and (x >=290 and x < 665):
                    break
                elif y-6 == 243 and not(x>330 and x<620):
                    break
                
                limite+=5
            limite=0
            while limite <= 130:
                x = int(JC.coords(luigi)[0])
                y = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(x,y,image=luigiizq,anchor =NW)
                JC.move(luigi,-1,6)
                JC.update()
                ventanaMenu.after(10)
                if y+6 == 513 or (y+6 == 405 and not(x >= 330 and x < 620)):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigiizq,anchor=NW)
                    break
                elif y+6 == 279 and not(x>229 and x<736):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigiizq,anchor=NW)
                    break
                elif y+6 == 279 and(x>285 and x<670):
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigiizq,anchor=NW)
                    break
                elif y+6 == 153 and not(x >= 330 and x < 620) :
                    JC.delete(luigi)
                    luigi = JC.create_image(x,y+6,image=luigiizq,anchor=NW)
                    break
                limite+=5
        limite=-1

def caer():
    global estadomario, JC, mario, juego, Xm, Ym
    if estadomario == "izquierda":
            limite = 0
            while limite <= 130:
                Xm = int(JC.coords(mario)[0])
                Ym = int(JC.coords(mario)[1])
                JC.delete(mario)
                mario = JC.create_image(Xm,Ym,image=marioizq,anchor =NW)
                JC.move(mario,0,6)
                JC.update()
                ventanaMenu.after(10)
                if Ym == 507 :
                    break
                elif Ym == 399:
                    break
                elif Ym == 273:
                    break
                limite += 5
    elif estadomario == "derecha":
            limite = 0
            while limite <= 130:
                Xm = int(JC.coords(mario)[0])
                Ym = int(JC.coords(mario)[1])
                JC.delete(mario)
                mario = JC.create_image(Xm,Ym,image=marioder,anchor =NW)
                JC.move(mario,0,6)
                JC.update()
                ventanaMenu.after(10)
                if Ym == 507 :
                    break
                elif Ym == 399:
                    break
                elif Ym == 273:
                    break
                limite += 5

def caerluigi():
    global estadoluigi, JC, luigi, juego, Xl, Yl
    if estadoluigi == "izquierda":
            limite = 0
            while limite <= 130:
                Xl = int(JC.coords(luigi)[0])
                Yl = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(Xl,Yl,image=luigiizq,anchor =NW)
                JC.move(luigi,0,6)
                JC.update()
                ventanaMenu.after(10)
                if Yl == 507 :
                    break
                elif Yl == 399:
                    break
                elif Yl == 273:
                    break
                limite += 5
    elif estadoluigi == "derecha":
            limite = 0
            while limite <= 130:
                Xl = int(JC.coords(luigi)[0])
                Yl = int(JC.coords(luigi)[1])
                JC.delete(luigi)
                luigi = JC.create_image(Xl,Yl,image=luigider,anchor =NW)
                JC.move(luigi,0,6)
                JC.update()
                ventanaMenu.after(10)
                if Yl == 507 :
                    break
                elif Yl == 399:
                    break
                elif Yl == 273:
                    break
                limite += 5

#Funciones Enemigos

#Shellcreeper:

def aparicion_Shell():
    print("llama aparicion shell 1")
    global shellverdeder,shellverdeizq, shell, juego, JC, estadoshell
    shell = JC.create_image(160,127,image=shellverdeder,anchor=NW)
    estadoshell = "derecha"
    Xs = JC.coords(shell)[0]
    Ys = JC.coords(shell)[1]
    
    cero = 0
    while cero <= 6:
        Xs = JC.coords(shell)[0]
        Ys = JC.coords(shell)[1]
        JC.delete(shell)
        shell = JC.create_image(Xs,Ys,image=shellverdeder,anchor=NW)
        JC.move(shell,0,6)
        JC.update()
        ventanaMenu.after(10)
        if Ys+6 == 163:
            break
        cero = cero + 1
    while cero <= 200:
        Xs = JC.coords(shell)[0]
        Ys = JC.coords(shell)[1]
        print(Xs,Ys)
        JC.delete(shell)
        shell = JC.create_image(Xs,Ys,image=shellverdeder,anchor=NW)
        JC.move(shell,5,0)
        JC.update()
        ventanaMenu.after(50-d)
        if Xs >= 995:
            JC.coords(shell,5,Ys)
        elif Ys == 163 and (Xs >= 326 and Xs<= 626):
            caerShell()
            cero = 0
        elif Ys == 289 and (Xs >= 665 and Xs <= 770):
            caerShell()
            cero = 0
        elif Ys == 289 and (Xs >= 225 and Xs<= 280):
            caerShell()
            cero =0 
        elif Ys == 415 and (Xs >= 330 and Xs <= 620):
            caerShell()
            cero = 0
        elif Ys == 523 and Xs == 810:
            JC.delete(shell)
            aparicion_Shell()
        cero += 1

def caerShell():
    global shell, juego, JC, estadoshell
    cero = 0
    while cero <= 6:
        Xs = JC.coords(shell)[0]
        Ys = JC.coords(shell)[1]
        JC.delete(shell)
        shell = JC.create_image(Xs,Ys,image=shellverdeder,anchor=NW)
        JC.move(shell,0,6)
        JC.update()
        ventanaMenu.after(10)
        if Ys+6 == 289:
            break
        elif Ys+6 == 415:
            break
        elif Ys+6 == 523:
            break

estadoshell2 = "creado"   
def aparicion_Shell2():
    global shellverdeder, mario, shellverdeizq, shell2, juego, JC, estadoshell2, vidasM, vidasL
    global d
    print("llama aparicion shell 2")
    shell2 = JC.create_image(780,127,image=shellverdeizq,anchor=NW)
    
        
    Xs2 = JC.coords(shell2)[0]
    Ys2 = JC.coords(shell2)[1]
    X2s2 = (JC.coords(shell2)[0])+60
    X1m = (JC.coords(mario)[0])+25
    Ym = (JC.coords(mario)[1])
    cero = 0
    while cero <= 6:
        Xs2 = JC.coords(shell2)[0]
        Ys2 = JC.coords(shell2)[1]
        JC.delete(shell2)
        shell2 = JC.create_image(Xs2,Ys2,image=shellverdeizq,anchor=NW)
        JC.move(shell2,0,6)
        JC.update()
        ventanaMenu.after(10)
        if Ys2+6 == 163:
            break
        cero = cero + 1
    
    while cero <= 200:
        X1s2 = JC.coords(shell2)[0]
        X2s2 = (JC.coords(shell2)[0])+60
        Ys2 = JC.coords(shell2)[1]
        X1m = (JC.coords(mario)[0])
        X2m = (JC.coords(mario)[0])+50
        Ym = (JC.coords(mario)[1])
        JC.delete(shell2)
        shell2 = JC.create_image(X1s2,Ys2,image=shellverdeizq,anchor=NW)
        JC.move(shell2,-5,0)
        print(X1s2,Ys2)
        JC.update()
        
        ventanaMenu.after(50-d)
        if X1s2 >= 995:
            JC.coords(shell,5,Ys2)
        elif X1s2 <= -5:
            JC.coords(shell2,990,Ys2)
        elif Ys2 == 163 and (X1s2 >= 326 and X1s2<= 615):
            caerShell2()
            cero = 0
        elif Ys2 == 289 and (X1s2 >= 665 and X1s2 <= 770):
            caerShell2()
            cero = 0
        elif Ys2 == 289 and (X1s2 >= 225 and X1s2<= 280):
            caerShell2()
            cero =0 
        elif Ys2 == 415 and (X1s2 >= 330 and X1s2 <= 620):
            caerShell2()
            cero = 0
        elif Ys2 == 523 and X1s2 == 135:
            JC.delete(shell2)
            aparicion_Shell2()
        elif estadoshell2 == "creado":
                    X1s2 = JC.coords(shell2)[0]
                    X2s2 = JC.coords(shell2)[0]+60
                    Ys2 = JC.coords(shell2)[1]
                    X1m = JC.coords(mario)[0]
                    X2m = JC.coords(mario)[0]+50
                    Ym = JC.coords(mario)[1]
                    if (Ym == 513 and Ys2 == 523) and ((X1s2-5 >= X2m and X1s2-5<= X2m) or (X2s2-5 <= X1m and X2s2-5 >= X1m)):
                        JC.delete(mario)
                        vidasM = vidasM -1
                        if vidasM < 0:
                            reaparecerMario()
                    elif (Ym == 405 and Ys2 == 415) and((X1s2-5 >= X2m and X1s2-5 <= X2m) or (X2s2-5 <= X1m and X2s2-5 >= X1m)):
                        JC.delete(mario)
                        vidasM = vidasM -1
                        if vidasM < 0:
                            reaparecerMario()
                    elif (Ym == 279 and Ys2 == 289) and ((X1s2-5 >= X2m and X1s2-5 <= X2m) or (X2s2-5 <= X1m and X2s2-5 >= X1m)):
                        JC.delete(mario)
                        vidasM = vidasM -1
                        if vidasM < 0:
                            reaparecerMario()
                    elif (Ym == 153 and Ys2 == 163) and ((X1s2-5 >= X2m and X1s2-5 <= X2m) or (X2s2-5 <= X1m and X2s2-5 >= X1m)):
                        JC.delete(mario)
                        vidasM = vidasM -1
                        if vidasM < 0:
                            reaparecerMario()
                    

        cero += 1
    if estadoshell2 == "destruido":
        return 'break'
def reaparecerMario():
    global mario, JC
    mario = JC.create_image(140,513,image=marioder,anchor=NW)
    estadomario = "derecha"
def caerShell2():
    global shellverdeder,shell2, juego, JC, estadoshell2
    cero = 0
    while cero <= 6:
            Xs2 = JC.coords(shell2)[0]
            Ys2 = JC.coords(shell2)[1]
            JC.delete(shell2)
            shell2 = JC.create_image(Xs2,Ys2,image=shellverdeizq,anchor=NW)
            JC.move(shell2,0,6)
            JC.update()
            ventanaMenu.after(10)
            if Ys2+6 == 289:
                break
            elif Ys2+6 == 415:
                break
            elif Ys2+6 == 523:
                break 

menu.pack()
ventanaMenu.mainloop()
