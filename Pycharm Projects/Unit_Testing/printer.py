class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, pages_per_s, capacity):
        self.pages_per_s = pages_per_s
        self._capacity = capacity


    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError("Capacity is less than given number of pages")

        self._capacity -= pages
        return f" Printed {pages} pages in {pages/self.pages_per_s:.2f} seconds"