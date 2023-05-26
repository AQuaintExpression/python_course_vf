from lxml import etree

# xml_string = """<root><item><name>Item 1</name><price>10.00</price></item><item><name>Item 2</name><price>20.00</price></item></root>"""

with open('example.xml') as f:
    xml_string = f.read()


root = etree.fromstring(xml_string)
print(etree.tostring(root, pretty_print=True).decode())
print('*******')
# Add a new item
new_item = etree.Element("item")
new_name = etree.SubElement(new_item, "name")
new_name.text = "Item 3"
new_price = etree.SubElement(new_item, "price")
new_price.text = "30.00"
root.append(new_item)

# Modify an existing item
item2 = root.xpath('//item[name="Item 2"]')[0]
item2_price = item2.xpath('price/text()')[0]
item2_price = str(float(item2_price) * 1.1)
item2.xpath('price')[0].text = item2_price

# Remove an item
item1 = root.xpath('//item[name="Item 1"]')[0]
root.remove(item1)

print(etree.tostring(root, pretty_print=True).decode())