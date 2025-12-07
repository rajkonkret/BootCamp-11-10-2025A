from xml.dom import minidom

DOMTree = minidom.parse("dane.xml")
print(DOMTree.toxml())
# <?xml version="1.0" ?><znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x104b49a30>]

znajomi = cNodes[0]
print("Znajomi:", cNodes)

persons = znajomi.getElementsByTagName("osoba")
print(persons[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>

print(persons[1].toxml())
# <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>

osoba = persons[0]
imie = osoba.getElementsByTagName("imie")[0]
print(imie)  # <DOM Element: imie at 0x105985d90>
imie1 = imie.firstChild.data
print(imie1)  # Zygmunt

atrybut = imie.getAttribute("foo")
print(atrybut)  # zzz, wartość dla atrybutu "foo"
