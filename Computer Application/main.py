import tkinter
from tkinter import *
import webbrowser
import helper
import tkinter.filedialog


def openfileEnc():
    filename = tkinter.filedialog.askopenfilename(
        initialdir="C:/Users/Jainish/Desktop", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    inputEncFileEntry.delete(0, END)
    inputEncFileEntry.insert(0, filename)


def opendirectoryEnc():
    directory = tkinter.filedialog.askdirectory(
        initialdir="C:/Users/Jainish/Desktop", title="Select directory")
    inputEncDirEntry.delete(0, END)
    inputEncDirEntry.insert(0, directory)


def openfileDec():
    filename = tkinter.filedialog.askopenfilename(
        initialdir="C:/Users/Jainish/Desktop", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    outputDecFileEntry.delete(0, END)
    outputDecFileEntry.insert(0, filename)


def opendirectoryDec():
    directory = tkinter.filedialog.askdirectory(
        initialdir="C:/Users/Jainish/Desktop", title="Select directory")
    outputDecDirEntry.delete(0, END)
    outputDecDirEntry.insert(0, directory)


def sendfilepage():
    webbrowser.open_new(r"http://127.0.0.1:5000/upload-file")


def recievefilepage():
    webbrowser.open_new(r"http://127.0.0.1:5000/file-directory")


def encryptor():
    EncryptBTN.config(state="disabled")
    public_key = publicKeyOfRecieverEntry.get()
    private_key = privateKeyOfSenderEntry.get()
    directory = inputEncDirEntry.get()
    filename = inputEncFileEntry.get()
    helper.encryption(filename, directory, public_key, private_key)


def decryptor():
    DecryptBTN.config(state="disabled")
    public_key = publicKeyOfSenderEntry.get()
    private_key = privateKeyOfRecieverEntry.get()
    directory = outputDecDirEntry.get()
    filename = outputDecFileEntry.get()
    helper.decryption(filename, directory, public_key, private_key)


def main():

    global filename
    global directory

    filename = ""
    directory = ""

    global form
    form = tkinter.Tk()
    form.wm_title('Secure file sharing')

    EncryptStep = LabelFrame(form, text=" 1. File Encryption: ", font=(
        'Helvetica 14 bold'), bd=5, background="black", foreground="orange")
    EncryptStep.grid(row=0, columnspan=7, sticky='W',
                     padx=5, pady=5, ipadx=5, ipady=5)

    DecryptStep = LabelFrame(form, text=" 2. File Decryption: ", font=(
        'Helvetica 14 bold'), bd=5, background="Black", foreground="orange")
    DecryptStep.grid(row=2, columnspan=7, sticky='W',
                     padx=5, pady=5, ipadx=5, ipady=5)

    menu = Menu(form)
    form.config(menu=menu)

    menufile = Menu(menu)
    menufile.add_command(label='Send file', command=lambda: sendfilepage())
    menufile.add_command(label='Recieve file',
                         command=lambda: recievefilepage())
    menufile.add_command(label='Exit', command=lambda: exit())
    menu.add_cascade(label='Menu', menu=menufile)

    global inputEncFileEntry
    global inputEncDirEntry
    global publicKeyOfRecieverEntry
    global privateKeyOfSenderEntry

    global EncryptBTN

    inputEncFile = Label(
        EncryptStep, text="Select the File:", background="black", foreground="yellow", font="bold")
    inputEncFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    inputEncFileEntry = Entry(EncryptStep, background="beige")
    inputEncFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    inputEncBtn = Button(EncryptStep, text="Browse ...",
                         command=openfileEnc, background="beige", foreground="black")
    inputEncBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    inputEncDir = Label(EncryptStep, text="Save File to:",
                        background="black", foreground="yellow", font="bold")
    inputEncDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    inputEncDirEntry = Entry(EncryptStep, background="beige")
    inputEncDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    inputEncDirBtn = Button(
        EncryptStep, text="Browse ...", command=opendirectoryEnc, background="beige", foreground="black")
    inputEncDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    publicKeyOfReciever = Label(EncryptStep, text="Public-Key of reciever:",
                                background="black", foreground="yellow", font="bold")
    publicKeyOfReciever.grid(row=2, column=0, sticky='E', padx=5, pady=2)

    publicKeyOfRecieverEntry = Entry(EncryptStep, background="beige")
    publicKeyOfRecieverEntry.grid(row=2, column=1, sticky='E', pady=2)

    privateKeyOfSender = Label(EncryptStep, text="Private-Key of sender:",
                               background="black", foreground="yellow", font="bold")
    privateKeyOfSender.grid(row=3, column=0, padx=5, pady=2)

    privateKeyOfSenderEntry = Entry(EncryptStep, background="beige")
    privateKeyOfSenderEntry.grid(row=3, column=1, pady=2)

    EncryptBTN = tkinter.Button(
        EncryptStep, text="Encrypt   ", command=encryptor, background="teal", foreground="black")
    EncryptBTN.grid(row=4, column=1, sticky='W', padx=5, pady=2)

    global outputDecFileEntry
    global outputDecDirEntry
    global publicKeyOfSenderEntry
    global privateKeyOfRecieverEntry

    global DecryptBTN

    outputDecFile = Label(DecryptStep, text="Select the File:",
                          background="black", foreground="yellow", font="bold")
    outputDecFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    outputDecFileEntry = Entry(DecryptStep, background="beige")
    outputDecFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    outputDecBtn = Button(DecryptStep, text="Browse ...",
                          command=openfileDec, background="beige", foreground="black")
    outputDecBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    outputDecDir = Label(DecryptStep, text="Save File to:",
                         background="black", foreground="yellow", font="bold")
    outputDecDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    outputDecDirEntry = Entry(DecryptStep, background="beige")
    outputDecDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    outputDecDirBtn = Button(
        DecryptStep, text="Browse ...", command=opendirectoryDec, background="beige")
    outputDecDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    publicKeyOfSender = Label(DecryptStep, text="Public-Key of sender:",
                              background="black", foreground="yellow", font="bold")
    publicKeyOfSender.grid(row=2, column=0, sticky='E', padx=5, pady=2)

    publicKeyOfSenderEntry = Entry(DecryptStep, background="beige")
    publicKeyOfSenderEntry.grid(row=2, column=1, sticky='E', pady=2)

    privateKeyOfReciever = Label(DecryptStep, text="Private-Key of reciever:",
                                 background="black", foreground="yellow", font="bold")
    privateKeyOfReciever.grid(row=3, column=0, padx=5, pady=2)

    privateKeyOfRecieverEntry = Entry(DecryptStep, background="beige")
    privateKeyOfRecieverEntry.grid(row=3, column=1, pady=2)

    DecryptBTN = tkinter.Button(
        DecryptStep, text="Decrypt   ", command=decryptor, background="teal", foreground="black")
    DecryptBTN.grid(row=4, column=1, sticky='W', padx=5, pady=2)

    form.mainloop()


if __name__ == "__main__":
    main()