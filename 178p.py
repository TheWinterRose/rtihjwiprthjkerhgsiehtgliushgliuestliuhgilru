from tkinter import*
import random
root=Tk()
root.title("Color")
root.geometry("460x460")
l=Label(root,font=("times",25,"bold"),bg="white")
l.place(relx=0.5,rely=0.5,anchor=CENTER)
class GR:
    def __init__(self):
        self.__score=0
        def updategame(self):
            self.t=["RoyalBlue","Moccasin","PeachPuff","Aquamarine","Teal"]
            self.tr=randiom.randint(0,4)
            self.c=["RoyalBlue","Moccasin","PeachPuff","Aquamarine","Teal"]
            self.cr=random.randint(0,4)
            l["text"]=self.t[self.tr]
            l["fg"]=self.c[self.cr]
obj1=GR()
btn=Button(root, text="START",command=obj1.updategame, bg="dark olive green", fg="white",
           relief=FLAT, padx=10, pady=1, font=("Arial",15))
root.mainloop()