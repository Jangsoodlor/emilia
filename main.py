# from curses import window
from rembg import remove
from PIL import Image as im
from datetime import datetime
from tkinter import *
from tkinter import filedialog

def getDateTimeStr():
    now = datetime.now()
    return now.strftime('%Y%m%d_%H%M%S')

def openfile():
    file_path = filedialog.askopenfile(filetypes=[('PNG Files', '.png'), ('JPEG Files', '.jpg')])
    return file_path.name

def bg_del():
    # str(input('insert your picture directory baka: '))
    input_path = openfile()
    img_dir = rf'{input_path}'
    output_path = 'testfile/' + getDateTimeStr() + '.png'
    img_open = im.open(img_dir)
    output = remove(img_open)
    output.save(output_path)

def bt1_click():
    bg_del()

window = Tk()
window.geometry = ('500*500')
window.config(bg='red')

bt1 = Button(text='NiHao', command=bt1_click)
bt1.pack(side='left')

mainloop()


