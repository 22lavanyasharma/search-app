# ===============  Importing Suitable Libraries ==========================
from tkinter import *                                                   
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import googlesearch   #pip install google
# ================== .............. End..........============================

# ================== .......... Window Components........ ============================

#creating main window
root = tk.Tk()
#title of window
root.title("Anya Search")
#window size
root.geometry("800x500")

root.resizable(0,0)

#window icon
root.iconbitmap('Google.ico')

# ========================== ............. End............ =====================

# ============================== Action Function Code Starts here ====================
def callback(url):
        webbrowser.open(url)

def search_query():
        
        query = text.get("1.0","end-1c")
        s = googlesearch.search(query, tld="co.in", num=10, stop=5, pause=2)
        # print(s)
        for j in s:
                # print(j)
                webbrowser.open(j)
         
        


#============================== .............. End ................. ===================


# ========================  Main Design Window ===============================

#label to create top  design
l1 = Label(root,bg="black",width=500,height=2)
l1.grid(sticky="w")

#apps logo
apps_logo = ImageTk.PhotoImage(Image.open('apps.jpg'))
d = Label(root, image = apps_logo,borderwidth=0)
d.place(x=15,y=11)
#apps label
apps = Label(root,text="Apps",bg="black",fg="yellow",cursor="hand2")
apps.place(x=40,y=10) 
apps.bind("<Button-1>",lambda e: callback("https://about.google/intl/en/products/?tab=wh"))



# drive logo
d_logo = ImageTk.PhotoImage(Image.open('Google drive.png'))
d = Label(root, image = d_logo,borderwidth=0)
d.place(x=95,y=11)
# drive label
drive = Label(root,text="Drive",bg="black",fg="yellow",cursor="hand2")
drive.place(x=120,y=10) 
drive.bind("<Button-1>",lambda e: callback("https://drive.google.com/"))


#youtube logo
yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
y = Label(root, image = yt_logo,borderwidth=0)
y.place(x=190,y=12)
#youtube label
yt =  Label(root,text="videos",bg="black",fg="yellow",cursor="hand2")
yt.place(x=220,y=10)
yt.bind("<Button-1>",lambda e: callback("https://www.youtube.com/"))


#Gmail logo
gm_logo = ImageTk.PhotoImage(Image.open('gmail.jpg'))
l2 = Label(root, image = gm_logo,borderwidth=0)
l2.place(x=310,y=12)

#Gmail label
gmail =  Label(root,text="mail",bg="black",fg="yellow",cursor="hand2")
gmail.place(x=340,y=10)
gmail.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))


#Gmail label
g = Label(root,text="mail",cursor="hand2")
g.place(x=630,y=50)
g.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))

#Images label
i = Label(root,text="Images",cursor="hand2")
i.place(x=670,y=50)
i.bind("<Button-1>",lambda e: callback("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))

#signin button
signin = Button(root,text="sign in",font=('roboto',10,'bold'),bg="yellow",fg="green",cursor="hand2")
signin.place(x=730,y=50) 
signin.bind("<Button-1>",lambda e: callback("http://google.com"))


#google logo
g_logo = ImageTk.PhotoImage(Image.open('google logo.png'))
l2 = Label(root, image = g_logo)
l2.place(x=290,y=190)

root.configure(bg='white')
#search box
text = Text(root,width=90,height=1,relief=RIDGE,font=('roboto',10,'bold'),borderwidth=6)
text.place(x=120,y=300)

#search button
search = Button(root, text="Search",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2",command=search_query)
search.place(x=390,y=390)



#===================== Load the Window =============================
root.mainloop()

#======================= End Code =====================================