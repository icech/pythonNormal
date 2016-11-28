#!/home/ch/anaconda/bin/python
# -*- coding: utf-8 -*-
#Author: Chen Hao

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement



class XML(object):

    def __init__(self,filename, xml_info):
        self.createXml(xml_info)
        self.book.write(filename, 'utf-8')
        # self.book.write('book2.xml','utf-8',True) #true is with xml declaration


    def createXml(self,xml_info):

        xml_info = dict()
        self.book = ElementTree()
        purOrder = Element('annotation')
        self.book._setroot(purOrder)

        child = Element(tag='folder')
        child.text = 'VOC2007'
        purOrder.append(child)

        child = Element(tag='filename')
        child.text = '000002.jpg'
        purOrder.append(child)

        child = Element(tag='source')
        SubElement(child, 'database').text = 'The VOC2007 Database'
        SubElement(child, 'annotation').text = 'PASCAL VOC2007'
        SubElement(child, 'image').text = 'flickr'
        SubElement(child, 'flickrid').text = '329145082'
        purOrder.append(child)

        child = Element(tag='owner')
        SubElement(child, 'flickrid').text = 'hiromori2'
        SubElement(child, 'name').text = 'Hiroyuki Mori'
        purOrder.append(child)

        child = Element(tag='size')
        SubElement(child, 'width').text = '335'
        SubElement(child, 'height').text = '500'
        SubElement(child, 'depth').text = '3'
        purOrder.append(child)

        child = Element(tag='segmented')
        child.text = '0'
        purOrder.append(child)

        child = Element(tag='object')
        SubElement(child, 'name').text = 'train'
        SubElement(child, 'pose').text = 'Unspecified'
        SubElement(child, 'truncated').text = '0'
        SubElement(child, 'difficult').text = '0'
        bndbox = SubElement(child, 'bndbox')
        SubElement(bndbox, 'xmin').text  = '139'
        SubElement(bndbox,'ymin').text = '200'
        SubElement(bndbox, 'xmax').text  = '207'
        SubElement(bndbox,'ymax').text = '301'
        purOrder.append(child)

        self.indent(purOrder)

    def indent(self,elem, level=0):
        i = "\n" + level * "    "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            for e in elem:
                self.indent(e, level + 1)
            if not e.tail or not e.tail.strip():
                e.tail = i
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
        return elem



#Define a main() function that prints a little greeting.
def main():
    filename = 'book1.xml'
    book = XML(filename)

#This is standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
