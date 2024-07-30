from tkinter import*
from PIL import Image,ImageTk
from random import randint

#main window
root= Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\stone-user.png"))
paper_img = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\paper-user.jpeg"))
scissor_img = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\scissor.jpeg"))
rock_img_comp = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\stone.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\paper.jpeg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open(r"c:\Users\madhu\OneDrive\mini_project\image\scissor-user.jpeg"))

#insert picture
user_label = Label(root , image = scissor_img, bg="#9b59b6")
comp_image = Label(root , image = scissor_img_comp, bg="#9b59b6")
comp_image.grid(row=1, column =0)
user_label.grid(row=1, column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore = Label(root, text=0 ,font=100, bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row = 1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root, font=50, bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update choice
def updateMessage(x):
    msg['text'] = X

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score +=1
    playerScore["text"] =str(score)

#update computer score

def updateCompScore():
    score = int(computerScore["text"])
    score +=1
    computerScore["text"] =str(score)

#check winner
def checkWin(Player,computer):
    if Player == computer:
        updateMessage("It's a tie!!! ")
    elif Player == "rock":
        if computer == "paper":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif Player == "paper":
        if computer == "scissor":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateUserScore()
    elif Player == "scissor":
        if computer == "rock":
            updateMessage("YOU LOOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN")
            updateCompScore()
    else:
        pass

#update choices

choices =["rock", "paper" , "scissor"]

def updateChoice(x):

    #for Computer
    compChoice =choices[randint(0,2)]
    if compChoice =="rock":
        user_label.configure(image=rock_img_comp)
    elif compChoice =="paper":
        user_label.configure(image=paper_img_comp)
    else:
        user_label.configure(image=scissor_img_comp)
        
     #for User

    if x =="rock":
        user_label.configure(image=rock_img)
    elif x =="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)
        
    
#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()



