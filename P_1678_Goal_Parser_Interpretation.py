text = "(al)G(al)()()G"
text2= "G()()()()(al)"
text3= "G()(al)"

def interpret(command):
    command = command.replace("()","o")
    command = command.replace("(al)", "al")
    print(command)
    return command

interpret(text3)




