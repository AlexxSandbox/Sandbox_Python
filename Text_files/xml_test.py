from xml.etree import ElementTree

tree = ElementTree.parse('students.xml')
# get xml root
root = tree.getroot()
print(root)  # <Element 'studentList' at 0x027EA3E8>
print(root.tag)  # studentList

# print child for root
for child in root:
    print(child.tag, child.attrib)  # student {'id': '1'}, student {'id': '2'}

# get value for child with index
print(root[0][0].text)  # Greg
print(root[1][1].text)  # Wood

# get all child for element using tag
for element in root.iter('scores'):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)  # 240.0, 240.2

# add value for module1
greg = root[1]
module1 = next(greg.iter('module1'))
module1.text = str(float(module1.text) + 30)

certificate = greg[2]
certificate.set('type', 'with distinction')
tree.write('students_copy.xml')

# create element
description = ElementTree.Element('description')
description.text = 'Showed escellent skills during the course'
greg.append(description)
tree.write('students_mod.xml')

# delete element
description = greg.find('description')
greg.remove(description)
tree.write('students_copy.xml')

# create tree
root = ElementTree.Element('student')

first_name = ElementTree.SubElement(root, 'firstName')
first_name.text = 'Greg'
last_name = ElementTree.SubElement(root, 'lastName')
last_name.text = 'Dean'

scores = ElementTree.SubElement(root, 'scores')

module_1 = ElementTree.SubElement(scores, 'module1')
module_1.text = '100'
# module_2 ...
# module_3 ...

tree = ElementTree.ElementTree(root)
tree.write('student.xml')
