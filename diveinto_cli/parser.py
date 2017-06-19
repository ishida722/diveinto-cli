from diveinto_cli.commands import *

def _Normalization(text):
    if not isinstance(text, str): return text
    return text.strip().split()

def GetCommand(rawInputText = None):
    inputText = _Normalization(rawInputText)

    if inputText is None:
        command = NoAct()

    elif inputText[0].isdigit() :
        command = Dive()
        command.arg1 = int(inputText[0])

    elif(inputText[0]=='r' or inputText[0]=='rise'):
        command = Rise()

    elif(inputText[0]=='l' or inputText[0]=='ls'):
        command = List()

    elif(inputText[0]=='q'):
        command = Quit()

    elif(inputText[0]=='d'):
        command = Delete()
        command.arg1 = [int(i) for i in inputText[1:]]

    else:
        command = Add()
        command.arg1 = rawInputText

    return command
