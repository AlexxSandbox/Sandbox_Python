from xml.etree import ElementTree


class Scores:
    depth = 0
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    def start(self, tag, attrib):
        self.depth += 1
        self.colors[attrib['color']] += self.depth

    def end(self, tag):
        self.depth -= 1

    def close(self):
        return self.colors['red'], self.colors['green'], self.colors['blue']


def get_scores():
    target = Scores()
    parser = ElementTree.XMLParser(target=target)
    xml_src = input()
    parser.feed(xml_src)
    print(*parser.close())


if __name__ == '__main__':
    get_scores()
