import unittest
# import shutil
# import os.path
# from diveinto.cli import Cli
# from diveinto.printer import printer
# import io
# import sys

class test_cli(unittest.TestCase):
    pass

    # def setUp(self):
    #     self.testDB = 'testdb.xml'
    #     printer.clear()
    #     self.cli = Cli(self.testDB)
    #     self.capture = io.StringIO()
    #     sys.stdout = self.capture

    # def tearDown(self):
    #     printer.printScreen()
    #     printer.clear()
    #     sys.stdout = sys.__stdout__
    #     if os.path.exists(self.testDB):
    #         os.remove(self.testDB)

    # def AssertTodoListLength(self, length):
    #     self.assertEqual(length, len(self.cli.db.GetCurrentList()))

    # def AssertTodoName(self, listNum, title):
    #     self.assertEqual(title, self.cli.db.GetCurrentList()[listNum].get('title'))

    # def AssertNoExistTask(self, listNum):
    #     try:
    #         self.dbCon.GetCurrentList()[listNum]
    #     except IndexError:
    #         self.assertTrue(True)
    #     self.assertTrue(False)

    # def test_AnalysisCommand(self):
    #     self.assertEqual("NoAct", self.cli.parser.Analysis(""))
    #     self.assertEqual("Add", self.cli.parser.Analysis("add task"))
    #     self.assertEqual("Move", self.cli.parser.Analysis("1"))

    # def test_AddTask(self):
    #     self.cli.Command('milk')
    #     self.AssertTodoName(1, 'milk')

    #     self.cli.Command('buy a meet')
    #     self.AssertTodoName(2, 'buy a meet')

    # def test_DiveIntoTask(self):
    #     self.cli.Command('Shopping List')
    #     self.AssertTodoName(1, 'Shopping List')

    #     self.cli.Command('1')
    #     self.cli.Command('milk')
    #     self.cli.Command('cake')

    #     self.AssertTodoName(1, 'milk')
    #     self.AssertTodoName(2, 'cake')

    # def test_DoneTask(self):
    #     self.cli.Command('Shopping List')
    #     self.cli.Command('home')
    #     self.cli.Command('job')
    #     self.AssertTodoName(1, 'Shopping List')

    #     self.cli.Command('d1')
    #     self.cli.Command('d2')

    #     self.cli.Command('l')

    # def test_DoneTaskTwice(self):
    #     self.cli.Command('Shopping List')
    #     self.AssertTodoName(1, 'Shopping List')

    #     self.cli.Command('d1')
    #     self.cli.Command('d1')

    #     self.cli.Command('l')

    # def test_Done0(self):
    #     self.cli.Command('d0')

    # def test_PrintTaskList(self):
    #     self.cli.Command('Shopping List')
    #     self.cli.Command('at home')
    #     self.cli.Command('at office')
    #     printer.printScreen()
    #     self.cli.Command('l')
    #     printer.printScreen()

    #     exceptPrintResult = []
    #     exceptPrintResult.append('--------------------------------------------------------------------------------')
    #     exceptPrintResult.append('[None]')
    #     exceptPrintResult.append('1: Shopping List')
    #     exceptPrintResult.append('2: at home')
    #     exceptPrintResult.append('3: at office')
    #     exceptPrintResult.append('--------------------------------------------------------------------------------')

    #     self.assertEqual(exceptPrintResult, printer.screen)

    # def test_NoPrint(self):
    #     self.cli.Command('task')
    #     printer.printScreen()
    #     printer.printScreen()
    #     self.assertFalse(printer.screen)

if __name__ == '__main__':
    unittest.main()
