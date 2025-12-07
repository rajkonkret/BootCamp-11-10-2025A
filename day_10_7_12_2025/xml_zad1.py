# xml - dane w tagach
# <quiz></quiz>
from xml.dom import minidom

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', "Python=to-Python")
xml.appendChild(productChild)

print(root) # <xml.dom.minidom.Document object at 0x105948530>
