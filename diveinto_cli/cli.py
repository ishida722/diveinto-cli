import readline
import sys
import os.path
from diveinto.db_controller import DBcon
import diveinto_cli.parser as parser
from diveinto_cli.commands import *
from diveinto_cli.config import Config

DB_NAME = '.diveinto'
dbCon = None
config = None

def Init():
    global dbCon
    global config
    config = Config()
    dbCon = DBcon()
    InitDbFile()
    with open(DB_NAME, 'r') as db:
        dbCon.MakeTree(db)
    Command.SetDbController(dbCon)
    RestoreCursor()

def RestoreCursor():
    dbCon.Move(config.dic['LastTaskId'])

def InitDbFile():
    if IsExistDbFile():
        if dbCon.IsDbFileBroken(DB_NAME):
            with open(DB_NAME, 'w') as db:
                dbCon.InitDbFile(db)
        else:
            return
    else:
        with open(DB_NAME, 'w') as db:
            dbCon.InitDbFile(db)

def IsExistDbFile():
    return os.path.isfile(DB_NAME)

def FirstPrint():
    print('START DiveInto!')
    command = List()
    command.Execution()
    command.Print()

def Loop(input_text):
    command = parser.GetCommand(input_text)
    result = command.Execution()
    command.Print()
    if dbCon.IsTreeDirty:
        with open(DB_NAME, 'wb') as db:
            dbCon.Commit(db)
    return result

def quit():
    global config
    config.dic['LastTaskId'] = dbCon.GetCurrentTaskId()
    config.Save()
    sys.exit()

def Main():
    Init()
    FirstPrint()
    isContinue = 1
    while isContinue:
        isContinue = Loop(input('>> '))
    quit()
    return 0

if __name__ == '__main__':
    Main()
