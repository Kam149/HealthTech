#!C:\Python37\python.exe

print("content-type:text/html")
print("")

from code import loadFile

menu = loadFile("menu.html")
login = loadFile("function.html")
footer = loadFile("footer.html")

data = menu + login+ footer

print(data)