import xmltodict
import json

# XML data as a string
xml_string = '''
<fruit>
    <name>apple</name>
    <color>red</color>
    <price>1.00</price>
</fruit>
'''

# Convert XML string to OrderedDict
xml_dict = xmltodict.parse(xml_string)

# Convert OrderedDict to JSON
json_data = json.dumps(xml_dict)

# Print the resulting JSON
print(json_data)