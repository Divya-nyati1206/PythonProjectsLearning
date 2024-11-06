from printer import Printer, PrinterError
from unittest import TestCase


class TestPrinter(TestCase):

    def setUp(self):   # make new printer object for every test... # class - only one object
        self.printer = Printer(2.0, 300)

    def test_printer_class(self):

        self.printer.print(25)

    def test_for_error(self):
        with self.assertRaises(PrinterError):
            self.printer.print(305)

    def test_equal_capacity(self):
        self.printer.print(self.printer._capacity)