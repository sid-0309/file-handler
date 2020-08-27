import datetime
import os
import img2pdf
from rename import rename

def check(a):
    try:
        int(a)
        return True
    except ValueError:return False
def correct(d):
    rename(d)
    name_lst = [i for i in os.listdir(d) if i.endswith(".png")]
name = input("filename: ")
d = input("dir: ")
if d == "":d = str(datetime.date.today())
if name == "": name = "final__"+str(datetime.date.today())
#ext = [".jpg", ".png", ".jpeg", ".bmp"]
name_lst = [i for i in os.listdir(d) if i.endswith(".png")]
for i in name_lst:
    part = i.partition(".")
    if check(part[0]) is True:
        continue
    else:correct(d)
with open(name+".pdf", "wb") as f:
    f.write(img2pdf.convert([d+"\\"+i for i in name_lst]))