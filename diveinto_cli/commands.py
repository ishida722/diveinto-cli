import sys

class Command(object):
    dbCon = None

    @classmethod
    def SetDbController(cls, db):
        cls.dbCon = db

    def __init__(self):
        self.arg1 = None
        self.output = []

    def Execution(self):
        return 1

    def Print(self):
        if len(self.output) == 0: return
        for i in self.output:
            print(i)

class NoAct(Command):
    pass

class Dive(Command):
    def Execution(self):
        self.dbCon.DiveInto(self.arg1)
        self.output.append('THERE IS {}'.format(self.dbCon.GetCurrentTaskName()))
        return 1

class Rise(Command):
    def Execution(self):
        self.dbCon.Rise()
        self.output.append('THERE IS {}'.format(self.dbCon.GetCurrentTaskName()))
        return 1

class List(Command):
    def Execution(self):
        self.output.append(self.dbCon.GetCurrentTaskName())
        for i, name in enumerate(self.dbCon.ChildTaskNames()):
            self.output.append('{} : {}'.format(i, name))
        return 1

class Quit(Command):
    def Execution(self):
        return 0

class Delete(Command):
    def Execution(self):
        deletedTaskNames = self.dbCon.DeleteTasks(*self.arg1)
        for taskName in deletedTaskNames:
            self.output.append('DELETE {}'.format(taskName))
        return 1

class Add(Command):
    def Execution(self):
        self.dbCon.AddTask(self.arg1)
        self.output.append('ADD {}'.format(self.arg1))
        return 1
