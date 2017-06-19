import unittest
import diveinto_cli.parser as parser

class parserTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_NoAct(self):
        command = parser.GetCommand()
        self.assertEqual('NoAct', command.__class__.__name__)

    def test_Dive(self):
        command = parser.GetCommand('1')
        self.assertEqual('Dive', command.__class__.__name__)
        self.assertEqual(1, command.arg1)

    def test_Rise(self):
        command = parser.GetCommand('r')
        self.assertEqual('Rise', command.__class__.__name__)

    def test_Rise2(self):
        command = parser.GetCommand('rise')
        self.assertEqual('Rise', command.__class__.__name__)

    def test_List(self):
        command = parser.GetCommand('l')
        self.assertEqual('List', command.__class__.__name__)

    def test_Quit(self):
        command = parser.GetCommand('q')
        self.assertEqual('Quit', command.__class__.__name__)

    def test_Delete(self):
        command = parser.GetCommand('d 1')
        self.assertEqual('Delete', command.__class__.__name__)
        self.assertEqual(1, command.arg1[0])

    def test_DeleteWithEndSpace(self):
        command = parser.GetCommand('d 1 ')
        self.assertEqual('Delete', command.__class__.__name__)
        self.assertEqual(1, command.arg1[0])

    def test_DeleteMulti(self):
        command = parser.GetCommand('d 1 13 4 56 ')
        self.assertEqual('Delete', command.__class__.__name__)
        self.assertEqual(1, command.arg1[0])
        self.assertEqual(13, command.arg1[1])
        self.assertEqual(4, command.arg1[2])
        self.assertEqual(56, command.arg1[3])

    def test_Add(self):
        command = parser.GetCommand('new task')
        self.assertEqual('Add', command.__class__.__name__)
        self.assertEqual('new task', command.arg1)
