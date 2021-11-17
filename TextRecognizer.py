import tkinter
from tkinter import *
import cv2
import pytesseract
import ctypes
import pyperclip
from tkinter import filedialog as fd

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'#teseract path

def FileDialogOpen():
    img = cv2.imread(tkinter.filedialog.askopenfilename())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config = r'--oem 3 --psm 6'
    canvas.create_text(200, 200, text="Recognized text copy to your clip board", font=(40))
    cv2.waitKey(0)
    #print(pytesseract.image_to_string(img, config=config))  # print the recognized text to the console
    ctypes.windll.user32.MessageBoxW(0, pytesseract.image_to_string(img, config=config), "Recognized Text", 1)#popup recognized text
    pyperclip.copy(pytesseract.image_to_string(img, config=config)) #copy recognized text to clip board

menu = Tk()
menu.title('Text Recognizer',)
menu.wm_attributes('-alpha')
menu.geometry('600x500')
menu.resizable(False, False)
menu.iconbitmap('1.ico')
bg = PhotoImage(file = "search_find_lupa_21889.png")


label1 = Label(menu, image = bg)
label1.place(x = 45, y =270)
canvas = Canvas(menu)
canvas.pack()


button1 = Button(menu, text='Upload Image', borderwidth=3, activebackground='Dodgerblue3', command=FileDialogOpen, font=('David', 15, 'bold'), foreground='black').place(x=240, y=400)
menu.mainloop()

