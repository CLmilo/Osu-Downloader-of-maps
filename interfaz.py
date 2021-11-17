from tkinter import *

import program.osudowngraphic as p

root=Tk()

root.title("Osu-Downloader")

# FUNCION BUSQUEDA
def pulsaboton():
    p.Iniciar_descarga(lcuadro_usuario.get(),lcuadro_contraseña.get(),var1.get(),lcuadro_otheruser.get(),var3.get(),lcuadro_parte.get(),var2.get(),var4.get())

# INICIANDO MIFRAME
miFrame=Frame()
miFrame.pack()
miFrame.config(bg="gray")
miFrame.config(width="650",height="350")
#texto usuario
lusuario=Label(miFrame, text="Usuario")
lusuario.place(x=50,y=50)
#input usuario
lcuadro_usuario=Entry(miFrame)
lcuadro_usuario.place(x=150,y=50)
#texto contraseña
lcontraseña=Label(miFrame, text="Contraseña")
lcontraseña.place(x=50,y=80)
#input contraseña
lcuadro_contraseña=Entry(miFrame)
lcuadro_contraseña.place(x=150,y=80)
lcuadro_contraseña.config(show="*")
#texto other user
lotheruser=Label(miFrame, text="Otro Usuario")
lotheruser.place(x=50,y=110)
#input other user
lcuadro_otheruser=Entry(miFrame)
lcuadro_otheruser.place(x=150, y=110)
#checkbox other user
var1=IntVar()
lcheckbox_ou = Checkbutton(miFrame,text="otro usuario",variable=var1, onvalue=1,offvalue=0)
lcheckbox_ou.place(x=360,y=110)
#checkbox with video
var2=IntVar()
lcheckbox_wv = Checkbutton(miFrame,text="con video",variable=var2, onvalue=1,offvalue=0)
lcheckbox_wv.place(x=360,y=50)
#checkbox automate
var3=IntVar()
lcheckbox_at = Checkbutton(miFrame,text="automático",variable=var3, onvalue=1,offvalue=0)
lcheckbox_at.place(x=360,y=140)
#checkbox verbose
var4=IntVar()
lcheckbox_v = Checkbutton(miFrame,text="más info",variable=var4, onvalue=1,offvalue=0)
lcheckbox_v.place(x=360,y=80)
#texto parte
lparte=Label(miFrame, text="Parte")
lparte.place(x=50,y=140)
#input parte
lcuadro_parte=Entry(miFrame)
lcuadro_parte.place(x=150, y=140)
#boton descarga
botonDescarga=Button(miFrame, text="Descargar", command=pulsaboton)
botonDescarga.place(x=50,y=170)
root.mainloop()