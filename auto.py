import os
import img2pdf
import shutil
dir = os.getcwd()

def rename(d, ext = ".jpg"):
    os.chdir(d)
    max = len(str(len([i for i in os.listdir() if i.endswith(ext)])))
    for i in os.listdir():
        print(i)
        print(os.getcwd())
        name = ""
        if not i.endswith(ext):continue
        part=i.partition(".")
        for j in part[0]:
            if j.isdigit():name+=j
        if len(name) < max: name = "0"*(max-len(name))+name
        os.rename(i, name+part[1]+part[2])

    os.chdir(dir)

def pdf(d,name, ext = ".jpg"):
    os.chdir(d)
    with open(name+".pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir() if i.endswith(ext)]))
    shutil.move(d+"\\"+name+".pdf", dir+"\\"+name+".pdf")

def main():
    '''
    folder = input("dir: ")
    pdfname = input("filename: ")
    ext = input("extention: ")
    '''
    folder = "E:\org2"
    pdfname = "test"
    ext = ".png"

    rename(folder) if ext == "" else rename(folder, ext)

    pdf(folder, pdfname) if ext == "" else pdf(folder, pdfname,ext)

main()