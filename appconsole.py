printed = ""

def myprint(text="",newline=True):
    global printed
    printed += text
    if newline:
        printed += "\n"

def printoutput():
    global printed
    x, printed = printed, ""
    return x