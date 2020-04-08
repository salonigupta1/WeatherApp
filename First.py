import tkinter
from django.templatetags.i18n import language

def login(userid, password):
    ursid = userid.get()
    print("Login Attempted" + ursid)
    
def register():
    print("Registered")

window = tkinter.Tk()
window.title("EduHub")
window.geometry('280x300')
window.configure(background = 'black')
userid = tkinter.StringVar()
password = tkinter.StringVar()
remember = tkinter.StringVar()
tkinter.Label(window, text='Welcome to EduHub', bg='black', fg='yellow').grid(row=0, column=0)
tkinter.Label(window, text='User ID', bg='black', fg='yellow').grid(row=1, column=0)
tkinter.Entry(window, textvariable = userid).grid(row=1, column=1)
tkinter.Label(window, text='Password', bg='black', fg='yellow').grid(row=2, column=0)
tkinter.Entry(window, show='*', textvariable = password).grid(row=2, column=1)
tkinter.Label(window, text='', bg='black', fg='yellow').grid(row=3, column=0)
tkinter.Button(window, text="Login",bg='yellow', fg='black', command =lambda: login(userid, password)).grid(row=4,column=0)
tkinter.Button(window, text="Register",bg='yellow', fg='black', command = register).grid(row=4,column=1)
tkinter.Checkbutton(window,text='Remember Me', variable=remember, onvalue='yes', offvalue='no').grid(row=3, column=1)


window.mainloop()