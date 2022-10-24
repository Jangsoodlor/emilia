# from curses import window
from rembg import remove
from PIL import Image as im
from datetime import datetime
from tkinter import *

def getDateTimeStr():
    now = datetime.now()
    return now.strftime('%Y%m%d_%H%M%S')

def bg_del():
    input_path = str(input('insert your picture directory baka: '))
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


