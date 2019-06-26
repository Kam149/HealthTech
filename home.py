#!C:\Python37\python.exe

print("content-type:text/html")
print("")

from code import loadFile

menu = loadFile("menu.html")
home = loadFile("home.html")
footer = loadFile("footer.html")

data = menu + home + footer

print(data)
