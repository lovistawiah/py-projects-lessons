import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Lovis Tawiah</name>
    <phone type="intl">
    +233 24 905 2339
    </phone>
    <email hide="yes" />
</person>
'''
tree = ET.fromstring(data)
print("Name: ", tree.find('name').text)
print("Name: ", tree.find('email').get('hide'))
