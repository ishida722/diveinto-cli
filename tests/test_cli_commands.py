import unittest
import io
from diveinto.db_controller import DBcon
from diveinto_cli.commands import *

class CliCommandTest(unittest.TestCase):

    def setUp(self):
        self.testDB = io.StringIO("<DiveInto name='root'>\n</DiveInto>\n")
        self.dbCon = DBcon()
        self.dbCon.MakeTree(self.testDB)
        Command.SetDbController(self.dbCon)

    def tearDown(self):
        self.testDB.close()

    def AssertTaskName(self, num, name):
        self.assertEqual(name ,self.dbCon.cursor[num].get('name'))

    def IsExistTask(self, num):
        try:
            self.dbCon.cursor[num]
        except:
            return False
        return True

    def test_AddTask(self):
        command = Add()
        command.arg1 = 'task1'
        command.Execution()
        self.AssertTaskName(0, 'task1')

    def test_DeleteTask(self):
        command = Add()
        command.arg1 = 'task1'
        command.Execution()
        self.AssertTaskName(0, 'task1')

        command = Delete()
        command.arg1 = [0]
        command.Execution()
        self.assertFalse(self.IsExistTask(0))

    def test_PrintList(self):
        self.dbCon.AddTask('task1')
        self.dbCon.AddTask('task2')
        self.dbCon.AddTask('task3')

        self.AssertTaskName(0, 'task1')
        self.AssertTaskName(1, 'task2')
        self.AssertTaskName(2, 'task3')

        command = List()
        command.Execution()

        expect_output =['root', '0 : task1', '1 : task2', '2 : task3']
        result = command.output
        self.assertEqual(expect_output, result)
