from tkinter import *

import tkinter.messagebox


#draw canvas
root=Tk()
root.title("Oliver's Tic-Tac-Toe")
w=Canvas(root,width=600,height=500,bd=0,highlightthickness=0)
w.pack()

color=0
position=[0,0,0,0,0,0,0,0,0]
gameover=0

#draw chessboard
w.create_rectangle(150,150,450,450)
w.create_rectangle(150,250,450,350)
w.create_rectangle(250,150,350,450)

#drop chess & check if the position have chess
def action(event):
    global color
    global color_modi
    global gameover

#check gameover
    if gameover==1:
        tkinter.messagebox.showinfo("Message:","Game Over!")
        return

#check mouse click position
    if event.x<150 or event.x>450 or event.y<150 or event.y>450:
        tkinter.messagebox.showinfo("Message:","Please click chessboard area!")
        return
    
    if color==0:
        color=1
        color_modi="red"
    else:
        color=0
        color_modi="green"

    if 150<event.x<250 and 150<event.y<250:
        if position[0]==0:
            w.create_oval(150,150,250,250,fill=color_modi)
            if color_modi=="red":
                position[0]=1
            else:
                position[0]=2     
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
                
    if 250<event.x<350 and 150<event.y<250:
        if position[1]==0:
            w.create_oval(250,150,350,250,fill=color_modi)
            if color_modi=="red":
                position[1]=1
            else:
                position[1]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 350<event.x<450 and 150<event.y<250:
        if position[2]==0:
            w.create_oval(350,150,450,250,fill=color_modi)
            if color_modi=="red":
                position[2]=1
            else:
                position[2]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return

    if 150<event.x<250 and 250<event.y<350:
        if position[3]==0:
            w.create_oval(150,250,250,350,fill=color_modi)
            if color_modi=="red":
                position[3]=1
            else:
                position[3]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 250<event.x<350 and 250<event.y<350:
        if position[4]==0:
            w.create_oval(250,250,350,350,fill=color_modi)
            if color_modi=="red":
                position[4]=1
            else:
                position[4]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 350<event.x<450 and 250<event.y<350:
        if position[5]==0:
            w.create_oval(350,250,450,350,fill=color_modi)
            if color_modi=="red":
                position[5]=1
            else:
                position[5]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 150<event.x<250 and 350<event.y<450: 
        if position[6]==0:
            w.create_oval(150,350,250,450,fill=color_modi)
            if color_modi=="red":
                position[6]=1
            else:
                position[6]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 250<event.x<350 and 350<event.y<450:
        if position[7]==0:
            w.create_oval(250,350,350,450,fill=color_modi)
            if color_modi=="red":
                position[7]=1
            else:
                position[7]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return
            
    if 350<event.x<450 and 350<event.y<450:
        if position[8]==0:
            w.create_oval(350,350,450,450,fill=color_modi)
            if color_modi=="red":
                position[8]=1
            else:
                position[8]=2
        else:
            tkinter.messagebox.showinfo("Message","Already have a chess here!")
            if color==1:
                color=0
            else:
                color=1
                return

    
#judge winner     
    if ((position[0]==position[1]==position[2]==1) or
       (position[3]==position[4]==position[5]==1) or
       (position[6]==position[7]==position[8]==1) or
       (position[0]==position[3]==position[6]==1) or
       (position[1]==position[4]==position[7]==1) or
       (position[2]==position[5]==position[8]==1) or
       (position[0]==position[4]==position[8]==1) or
       (position[2]==position[4]==position[6]==1)):
        tkinter.messagebox.showinfo("Message:","Red Win!!!")
        gameover=1
    elif ((position[0]==position[1]==position[2]==2) or
          (position[3]==position[4]==position[5]==2) or
          (position[6]==position[7]==position[8]==2) or
          (position[0]==position[3]==position[6]==2) or
          (position[1]==position[4]==position[7]==2) or
          (position[2]==position[5]==position[8]==2) or
          (position[0]==position[4]==position[8]==2) or
          (position[2]==position[4]==position[6]==2)):
        tkinter.messagebox.showinfo("Message:","Green Win!!!")
        gameover=1
    else:
        if (position[0]!=0 and position[1]!=0 and position[2]!=0
            and position[3]!=0 and position[4]!=0 and position[5]!=0
            and position[6]!=0 and position[7]!=0 and position[8]!=0):
            tkinter.messagebox.showinfo("Message:","Equal!!!")
            gameover==1


#bind action
w.bind("<Button-1>",action)

w.mainloop()
