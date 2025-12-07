# xml - dane w tagach
# <quiz></quiz>
from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>

xml = root.createElement('root')
root.appendChild(xml)  # <root>

productChild = root.createElement('product')
productChild.setAttribute('name', "Python=to-Python")
xml.appendChild(productChild)  # <product name="Python=to-Python"/>

print(root)  # <xml.dom.minidom.Document object at 0x105948530>

xmlStr = root.toprettyxml()
print(xmlStr)
# <xml.dom.minidom.Document object at 0x10a0dc350>
# <?xml version="1.0" ?>
# <root>
# 	<product name="Python=to-Python"/>
# </root>

with open("ptp.xml", "w") as f:
    f.write(xmlStr)
