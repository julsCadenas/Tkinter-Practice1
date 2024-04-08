from customtkinter import *

def buttonClick():
    label = CTkLabel(master=app, text="haha ur mom gay", font=customFont)
    label.place(relx=0.5, rely=0.5, anchor="center")
    textAnimation(label)

def textAnimation(label):
    targetY=0.39
    currentY=float(label.place_info()['rely'])
    if currentY>targetY:
        label.place(rely=currentY-0.01)
        app.after(7, textAnimation, label)
    else:
        label.place_configure(rely=targetY, anchor="center")

app = CTk()
app.geometry("500x400")
app.title("urmom")

app.iconbitmap('chad.ico')

customFont = ("Helvetica", 20, "bold")

btn = CTkButton(master=app, text="ur mom", fg_color="#9966CC", hover_color="#5E5A80", corner_radius=32, font=customFont)
btn.place(relx=0.5, rely=0.5, anchor="center")
btn.configure(command=buttonClick)

app.mainloop()
