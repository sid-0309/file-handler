def rename(d = "."):
    import os
    files = os.listdir(d)
    for i in files:
        if not i.endswith(".png"):break
        part = i.partition(".")
        namem = part[0]
        name = ""
        for j in namem:
            if j.isdigit():name +=j
        os.rename(d+"\\"+i, name+part[1]+part[2])

    files = os.listdir(d)
    max = 0
    for i in files:
        if not i.endswith(".png"):break
        part = i.partition(".")
        if len(part[0]) > max: max = len(part[0])

    print(max)

    for i in files:
        if not i.endswith(".png"):break
        name = ""
        part = i.partition(".")
        print(part[0])
        if len(part[0]) <max: name = "0"*(max-len(part[0])) + part[0]
        print(name)
        if name == "":continue
        os.rename(d+"\\"+i, name+part[1]+part[2])
		
rename()