from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Devloper:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Devloper")


        title_lbl = Label(self.root, text="DEVLOPER",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)



        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)  # Note: Image.Resampling.LANCZOS may change to Image.LANCZOS based on PIL version
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # Use a different variable for the top image

        # Create the label for the top image and place it
        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=720) 

        # Frame 
        main_frame=Frame(f_lbl_top,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"college_images\Faceimage.jpg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)  # Note: Image.Resampling.LANCZOS may change to Image.LANCZOS based on PIL version
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)  # Use a different variable for the top image

        # Create the label for the top image and place it
        f_lbl_top = Label(main_frame, image=self.photoimg_top1)
        f_lbl_top.place(x=300, y=0, width=200, height=200)

        # Devloper info 
        dev_label=Label(main_frame,text="Hello Welcome to the devloper Section!!!!",font=("Times New Roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Hello Welcome to the devloper Section!!!!",font=("Times New Roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=40)


        img_top2 = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top2 = img_top2.resize((500, 390), Image.LANCZOS)  # Note: Image.Resampling.LANCZOS may change to Image.LANCZOS based on PIL version
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)  # Use a different variable for the top image

        # Create the label for the top image and place it
        f_lbl_top = Label(main_frame, image=self.photoimg_top2)
        f_lbl_top.place(x=0, y=210, width=500, height=390)

        

if __name__ == "__main__":
    root = Tk()
    obj = Devloper(root)
    root.mainloop()
      