from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from  face_recognition import Face_Recognitions
from attendece import Attendance
from devloper import Devloper
from help import Help
from tkinter import messagebox
from bot2 import ChatBot



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(r"college_images\Stanford.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image      
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"college_images\u.jpg")
        img2 = img2.resize((530, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=530, height=130)

        # Background Image
        img3 = Image.open(r"college_images\wp2551980.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First row - Buttons
        # Student Button
        img4 = Image.open(r"college_images\student.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Detail",command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector Button
        img5 = Image.open(r"college_images\Faceimage.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data,)
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Desk Button
        img7 = Image.open(r"college_images\help-desk-customer.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data,)
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Second row - Buttons
        # Train Button
        img8 = Image.open(r"college_images\train.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=400, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=600, width=220, height=40)

        # Photo Button 
        img9 = Image.open(r"college_images\Photos.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        # b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command==self.open_ing)
        # b6.place(x=500, y=400, width=220, height=220)

        # b6_1 = Button(bg_img, text="Photos", cursor="hand2",command==self.open_ing,
        #               font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b6_1.place(x=500, y=600, width=220, height=40)
        # Create a button with an image
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_ing)
        b6.place(x=500, y=400, width=220, height=220)

        # Create a second button with text
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_ing,
                    font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=600, width=220, height=40)


        # Devloper Button 
        img10 = Image.open(r"college_images\chat.jpg")
        img10= img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.bot_data)
        b7.place(x=800, y=400, width=220, height=220)

        b7_1 = Button(bg_img, text="Chat Bot", cursor="hand2",command=self.bot_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=600, width=220, height=40)

        # Exit Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iexit,)
        b8.place(x=1100, y=400, width=220, height=220)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iexit,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=600, width=220, height=40)


    def open_ing(self):
         os.startfile("data")   

    def iexit(self):
        self.iexit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?",parent=self.root)
        if self.iexit:  # 'askyesno' returns True or False, no need to compare with 0
                self.root.destroy()
        else:
                return
        #===============function Button==================
    
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)


    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognitions(self.new_window)


    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def bot_data(self):
            self.new_window=Toplevel(self.root)
            self.app=ChatBot(self.new_window)

    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()