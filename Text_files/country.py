from xml.etree import ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
# print(root.tag)


def get_root_child():
    """ get child for root """
    for child in root:
        print(child.tag, child.attrib)


def get_index_child():
    """ get child using index """
    print(root[0][0].text)  # 1
    print(root[0][1].text)  # 2008


def get_iter():
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)

    for r in root.iter('rank'):
        print(r.text)


def get_findall():
    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(rank, name)


def add_rank():
    """
    1 - increase rank to value
    2 - write new attribute 'update' with value 'yes'
    3 - create new file 'output.xml'
    """
    for rank in root.iter('rank'):
        new_rank = int(rank.text) + 1
        rank.text = str(new_rank)
        rank.set('update', 'yes')
    tree.write('output.xml')


def del_element():
    """
    delete element with rank more than 50
    1 - findall country
    2 - find rank in country
    3 - delete country with rank > 50
    4 - create new file 'output.xml'
    """
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank > 50:
            root.remove(country)
    tree.write('output.xml')


def create_et():
    root = ET.Element('a')
    b = ET.SubElement(root, 'b')
    c = ET.SubElement(root, 'c')
    d = ET.SubElement(c, 'd')
    tree = ET.ElementTree(root)
    tree.write('output.xml')


create_et()
