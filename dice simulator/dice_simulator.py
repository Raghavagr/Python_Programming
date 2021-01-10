import tkinter
from PIL import Image, ImageTk
import random

#print(random.randint(1,10))

#build a top-level widget which represent main window of application
root = tkinter.Tk()
root.geometry('400x400')
root.title("Crazy_Tech Roll the dice")

#now we will add an image area and label
#the number which is choosen by random no. that image we have to show.
#adding label into frame
blankLine = tkinter.Label(root, text="")
blankLine.pack()

#add headingLabel with text
HeadingLabel = tkinter.Label(root, text="Hello from Crazy_Tech", 
            fg="red", bg="black", font="Helvetica 16 bold italic")
HeadingLabel.pack()

#make a list of dice images
dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

#choose a random image from list and display that image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage  #save the refrence

#pack the image in parent widget
ImageLabel.pack(expand=True)

# we will show 1 default image on screen,
#  after that display we have to give button to roll dice and call func
#function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #update image in ImageLabel widget
    ImageLabel.configure(image=DiceImage)
    #keep a refrence
    ImageLabel.image = DiceImage

#adding a button and cmd will use rolling_dice function
button = tkinter.Button(root, text="Roll the Dice", fg="black", bg="light blue", command=rolling_dice)
#pack the widget in parent widget
button.pack(expand=True)

#call the mainloop of window
root.mainloop()
