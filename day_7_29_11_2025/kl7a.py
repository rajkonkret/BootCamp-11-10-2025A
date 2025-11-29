from pprint import pprint


class Printer:
    def print_message(self, message):
        print(f'Drukowanie wiadomości: {message}')


class Scanner:
    def scan_document(self):
        print("skanowanie dokumentu")
        return "Zawartośc dokumentu"


printer = Printer()
printer.print_message("Radek")
# Drukowanie wiadomości: Radek

scanner = Scanner()
print(scanner.scan_document())


# Zawartośc dokumentu
# mixin
class MultifunctionDevice(Printer, Scanner):

    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


device = MultifunctionDevice()
device.photocopy()
# skanowanie dokumentu
# Drukowanie wiadomości: Zawartośc dokumentu

message = device.scan_document()
print(message)
# skanowanie dokumentu
# Zawartośc dokumentu

device.print_message(message)
# Zawartośc dokumentu
# Drukowanie wiadomości: Zawartośc dokumentu

pprint(MultifunctionDevice.__mro__)
# (<class '__main__.MultifunctionDevice'>,
#  <class '__main__.Printer'>,
#  <class '__main__.Scanner'>,
#  <class 'object'>)