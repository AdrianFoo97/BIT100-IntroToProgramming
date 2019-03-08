# B1600693
# Adrian Foo Jun Wei
#import all thing from tkinter library
#import tkinter messagebox function
#import tkinter dialog function
#import tkinter random function
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import random


# function to create a window when 'play' button on the main interface is clicked------------------------------------------------------------
def create_windowplay():
    global boardwindow
    #minimize the root window when 'play' button is clicked
    root.iconify()
    #call a new window (boardwindow) for board
    boardwindow = Toplevel(root)
    boardwindow.resizable(width=False, height=False)
    boardwindow.configure(background='#ecf0f1')
    #call board function and dice window
    dice()
    gameboard()
    

#function to recall board and dice function to have variable changes. Used as command when click on the 'rolldice' button
def recall_dice_board():
    rolldice()
    gameboard()
   
# board function (created by using for loop with grid)
def gameboard():
    global position
    gridnum=1
    for r in range(1,6,1):
        for c in range(1,11,1):
            # To let the row start from down, r is used as 6-r, and column is c which start from left to right
            if r==1 or r==3 or r==5:
                gridlabel = Label(boardwindow, text=gridnum, borderwidth=50,font="Courier 20 bold",bg="black",fg="white", height=1, width=1) 
                gridlabel.grid(row=6-r,column=c,padx=1,pady=1)

                #change color for the ladder
                if gridnum==ladder1 or gridnum==ladder_1 or gridnum==ladder2 or gridnum== ladder_2 or gridnum==ladder3 or gridnum==ladder_3 or gridnum==ladder4 or gridnum==ladder_4:
                    gridlabel.config(bg="#0033FF")
                    
                    if gridnum==ladder1 or gridnum==ladder_1:
                        gridlabel.config(fg="#00FF66")
                    if gridnum==ladder2 or gridnum==ladder_2:
                        gridlabel.config(fg="#CCCCCC")
                    if gridnum==ladder3 or gridnum==ladder_3:
                        gridlabel.config(fg="#FF6600")
                    if gridnum==ladder4 or gridnum==ladder_4:
                        gridlabel.config(fg="#FD1C03")
                        
                #change color for the snake
                if gridnum==snake1 or gridnum==snake_1 or gridnum==snake2 or gridnum==snake_2 or gridnum==snake3 or gridnum==snake_3:
                    gridlabel.config(bg="#FF0000")
                    if gridnum==snake1 or gridnum==snake_1:
                        gridlabel.config(fg="#099FFF")
                    if gridnum==snake2 or gridnum==snake_2:
                        gridlabel.config(fg="#FFCC00")
                    if gridnum==snake3 or gridnum==snake_3:
                        gridlabel.config(fg="#E6FB04")

                #change color for the player current position when the postion from the dice function equal to the gridnumber from the board        
                if gridnum==position:
                    gridlabel.config(bg="grey",fg="yellow")

                #shows the players position when at final destination and close the board and dice window and reset the postition to 0  
                if gridnum==position==final:
                    gridlabel.config(bg="grey",fg="yellow")
                    tkinter.messagebox.showinfo("","Congratualations! You have reach the destination!")
                    boardwindow.destroy()
                    dicewindow.destroy()
                    root.deiconify()
                    position=0
                #after first loop, gridnum is added by 1 so the gridnum at the second loop will increase
                gridnum = gridnum+1

            # To let the row start from down, r is used as 6-r, and column is 11-c which start from right to left
            elif r==2 or r==4:
                gridlabel=Label(boardwindow,text=gridnum, borderwidth=50,font="Courier 20 bold",bg="black",fg="white", height=1, width=1)
                gridlabel.grid(row=6-r,column=11-c,padx=1,pady=1)

                #change color for the ladder
                if gridnum==3 or gridnum==8 or gridnum==6 or gridnum== 26 or gridnum==14 or gridnum==22 or gridnum==32 or gridnum==49:
                    gridlabel.config(bg="#0033FF")
                    if gridnum==ladder1 or gridnum==8:
                        gridlabel.config(fg="#00FF66")
                    if gridnum==ladder2 or gridnum==26:
                        gridlabel.config(fg="#CCCCCC")
                    if gridnum==ladder3 or gridnum==22:
                        gridlabel.config(fg="#FF6600")
                    if gridnum==ladder4 or gridnum==49:
                        gridlabel.config(fg="#FD1C03")

                #change color for the snake       
                if gridnum==48 or gridnum==44 or gridnum==39 or gridnum== 34 or gridnum==28 or gridnum==13:
                    gridlabel.config(bg="#FF0000")
                    if gridnum==snake1 or gridnum==44:
                        gridlabel.config(fg="#099FFF")
                    if gridnum==snake2 or gridnum==34:
                        gridlabel.config(fg="#FFCC00")
                    if gridnum==snake3 or gridnum==13:
                        gridlabel.config(fg="#E6FB04")
                        
                #change color for the player current position when the postion from the dice function equal to the gridnumber from the board 
                if gridnum==position:
                    gridlabel.config(bg="grey",fg="yellow")

                #shows the players position when at final destination and close the board and dice window and reset the postition to 0     
                if gridnum==position == final:
                    gridlabel.config(bg="grey",fg="yellow")
                    tkinter.messagebox.showinfo("","Congratualations! You have reach the destination!")
                    boardwindow.destroy()
                    dicewindow.destroy()
                    position=0
                #after first loop, gridnum is added by 1 so the gridnum at the second loop will be increased by 1
                gridnum = gridnum+1

                
                

#dice window function
def dice():
    global dicewindow
    global label_dicenumber
    global label_diceposition
    #create a window call dicewindow
    dicewindow = Toplevel(root)
    dicewindow.configure(background='black')
    dicewindow.resizable(width=False, height=False)
    
    #creating label in the dicewindow and the 'rolldice' button to call the 'recall_dice_board' which change the variable
    label_dicetext = Label(dicewindow, text="Dice Number:", font="Courier 14 ", fg="#00FF00", bg="black")
    label_dicetext.grid(row=0)
    label_dicenumber = Label(dicewindow,text="", fg="#00FF00", font="Courier 20 bold", bg="black")
    label_dicenumber.grid(row=1,pady=4)
    label_diceposition = Label(dicewindow,text="", fg="#00FF00", font="Courier 15", bg="black")
    label_diceposition.grid(row=2)
    button = Button(dicewindow, text='Roll Dice', font="Courier 14", width=25, fg="black", bg="#00FF00", command=recall_dice_board)
    button.grid(row=3)
                         
#rolldice with random.randiant
#declaring fixed data
ladder1 = 3
ladder_1 = 8
ladder2 = 6
ladder_2 = 26
ladder3 = 14
ladder_3 = 22
ladder4 = 32
ladder_4 = 49
snake1 = 48
snake_1 = 44
snake2 = 39
snake_2 = 34
snake3 = 28
snake_3 = 13
final = 50
dicenum = 0
position = 0

#function of dice to generate random number and set the postition according to the snake and ladder
def rolldice():
    global dicewindow
    global dicenumber
    global position
    global label_dicenumber
    global label_diceposition
    #generate random number from 1 to 6
    dicenum = random.randint(1,6)
    #change the dice number in the label 'label_dicenumber'
    label_dicenumber.config(text=str(dicenum))
    position = position + dicenum
    if position <=50:
    #change the dice original position in the label 'label_diceposition
        label_diceposition.config(text="You have roll to "+ str(position))
    else:
        label_diceposition.config(text="You have roll to "+ str(50-(position-50)))
    #when the position equal to the snake and ladder, the player's position will be change to particular number
    if position == snake1:
            position =snake_1
            tkinter.messagebox.showinfo("","Opps! You meet a snake")
                
    if position == snake2:
            position =snake_2
            tkinter.messagebox.showinfo("","Opps! You meet a snake")
                
    if position == snake3:
            position =snake_3
            tkinter.messagebox.showinfo("","Opps! You meet a snake")
                
    if position == ladder1:
            position =ladder_1
            tkinter.messagebox.showinfo("","A ladder for you.")
                
    if position == ladder2:
            position =ladder_2
            tkinter.messagebox.showinfo("","A ladder for you.")
                
    if position == ladder3:
            position =ladder_3
            tkinter.messagebox.showinfo("","A ladder for you.")
                
    if position == ladder4:
            position =ladder_4
            tkinter.messagebox.showinfo("","A ladder for you.")

    #when the position count is larger than 50, the position will change according the formula        
    if position > final:
            position = 50-(position-50)
    #when position is equal to 50, close the dice window
    if position ==final:
            dicewindow.destroy()
            
#function to create a window for introduction message----------------------------------------------------------------------------------------------------------------------------------------
def create_windowintro():
    #create a new window call introwindow
    introwindow = Toplevel(root)
    introwindow.geometry("450x330")
    introwindow.resizable(width=False, height=False)
    #insert a label used as title which fill the horizontal space
    label_intro = Label(introwindow, text="Introduction", justify="center", font="Times 24 bold", bg="#000000", fg="#00FF00")
    label_intro.pack(fill=X)
    #Adding the introduction using the message widget
    introtext=Message(introwindow, font="Times 20", bg="#000000",fg="#00FF00", text = "      Snakes and Ladders is an ancient Indian board regarded today \
as a worldwide classic.A number of 'ladders' and 'snakes' are pictured on the board, each connecting two specific board squares. The object of the game is \
to navigate one's piece,from the start to the finish, helped or hindered by ladders and snakes respectively.")
    introtext.pack()


# function to create a feedback window -----------------------------------------------------------------------------------------------------------------------------------   
 
def create_windowfeedback():
    #create a window to ask for user input using simpledialog function
    feedback = tkinter.simpledialog.askstring("", "Please give us your comment")
    #create a feedback window to user using messagebox widget
    tkinter.messagebox.showinfo("","Thanks for your feedback")
    
#Function for destroy the mainloop()----------------------------------------------------------------------------------------------------------------------------------
def quit():
    #create a window to ask user to quit with the "messagebox.askquestion" function
    answer = tkinter.messagebox.askquestion("Quit", "Do you really want to quit?")
    if answer == 'yes':
        root.destroy()
    
    



#main window--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create the main user interface window which is unresizable with fixed width and height
root = Tk()
root.title("Snakes And Laders")
root.geometry("600x250")
root.resizable(width=False, height=False)
root.configure(background='black')

#A frame for label and button arrangement
frame1 = Frame(root, bg="#000000")
frame1.pack(side=BOTTOM)

#inseting a logo image in a label 
logophoto = PhotoImage(file="logo.gif", format="gif -index 3")
label_logo = Label(root, image=logophoto)
label_logo.pack()

#button to call 'create_windowplay' function which create a boardwindow and dicewindow
btn_play = Button(frame1,text="Play", bg="#00FF00",fg="#000000",
             font="Courier 16 bold", width=12, height=2, relief=FLAT,
            command=create_windowplay)
btn_play.grid(row=0, column=0, pady=8, padx=8)

#button to call 'create_windowintro' function which create a window with introduction
btn_intro = Button(frame1,text="Introduction", bg="#00FF00",fg="#000000",
                font="Courier 16 bold", width=12, height=2,relief=FLAT,
                command=create_windowintro)
btn_intro.grid(row=0, column=1, pady=8, padx=8)  

#button to call 'create_windowfeedback' function which create a dialogbox for user input
btn_feedback = Button(frame1,text="Feedback", bg="#00FF00",fg="#000000",
                font="Courier 16 bold", width=12, height=2,relief=FLAT,
                command=create_windowfeedback)
btn_feedback.grid(row=1, column=0, pady=8, padx=8)

#button to call 'quit' function which create a message box to ask for quit 
btn_exit = Button(frame1,text="Exit", bg="#00FF00",fg="#000000",
                font="Courier 16 bold", width=12, height=2,relief=FLAT,
                command=quit)
btn_exit.grid(row=1, column=1, pady=8, padx=8)

#creating a pop up message after the main interface has run finish
#ask for user input for name using the simple dialog function
name = tkinter.simpledialog.askstring("","What is your name?")
output = "Hello, %s! Welcome to the Snakes and Ladders Game!" %(name)
#shows feedback to the user with the name that has been input using the messagebox.showinfo function
tkinter.messagebox.showinfo("Welcome!", output)

root.mainloop()

