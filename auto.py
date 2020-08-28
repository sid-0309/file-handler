import os
import img2pdf
import shutil
dir = os.getcwd()
def rename(d, r, ext = ".jpg"):
    global name_map
    os.chdir(d)
    max = len(str(len([i for i in os.listdir() if i.endswith(ext)])))
    name_map = {}
    for i in os.listdir():
        name = ""
        if not i.endswith(ext):continue
        part=i.partition(".")
        for j in part[0]:
            if j.isdigit():name+=j
        name = "0"*(max-len(name)) + name
        if r == "" or r == "n":
            name_map[f"{name}{part[1]}{part[2]}"] = i
            continue
        else:os.rename(i, name+part[1]+part[2])
def pdf(d, t, ext = ".jpg"):
    pdfname = input("filename: ")
    if t == 1:lst = [name_map[i] for i in sorted(name_map)]
    else:lst = [i for i in os.listdir() if i.endswith(ext)]
    with open(pdfname+".pdf", "wb") as f:
        f.write(img2pdf.convert(lst))
    shutil.move(d+"\\"+pdfname+".pdf", dir+"\\"+pdfname+".pdf")
def main(mode):
    folder = input("dir: ")
    ext = input("extention: ")
    if mode == 1:rename(folder,"y") if ext == "" else rename(folder, "y", ext)
    elif mode ==2:
        rename(folder, "n") if ext == "" else rename(folder, "n", ext)
        pdf(folder,1) if ext =="" else pdf(folder,1,ext)
    else:
        rename(folder,"y") if ext == "" else rename(folder, "y", ext)
        pdf(folder,2) if ext =="" else pdf(folder,2,ext)
print("Choose 1 for renaming numerically")
print("Choose 2 to convert to pdf")
print("Choose 3 for both")
print("Enter x to exit")
while True:
    mode_select = str(input("Choice: "))
    if mode_select == "x":break
    if mode_select == "":mode_select="2"
    if mode_select not in "123":
        print("Invalid Choice!")
        print("Choose 1 for renaming numerically")
        print("Choose 2 to convert to pdf")
        print("Choose 3 for both")
        print("Enter x to exit")
        mode_select = input("Choice: ")
        if mode_select == "":mode_select=2
        if mode_select == "x":break 
    main(int(mode_select))
    print("\n"*3)