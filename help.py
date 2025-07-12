from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help")



        title_lbl = Label(self.root, text="Help Desk",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)



        img_top = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)  # Note: Image.Resampling.LANCZOS may change to Image.LANCZOS based on PIL version
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # Use a different variable for the top image

        # Create the label for the top image and place it
        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=720) 


        dev_label=Label(f_lbl_top,text="Email:easepresence.co@gmail.com",font=("Times New Roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=200)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()