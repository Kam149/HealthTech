#!C:\Python37\python.exe

print("content-type:text/html")
print("")

from code import loadFile

menu = loadFile("menu.html")
state = loadFile("states.html")
footer = loadFile("footer.html")

data = menu + state + footer

print(data)