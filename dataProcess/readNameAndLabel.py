#!/home/ch/anaconda/bin/python
# -*- coding: utf-8 -*-
#Author: Chen Hao
import numpy as np
import re

# class labeledImage(object):
#     def __init__(self, name, label):
#         self.num_object = 0
#         self.name = name
#         for item in label:


def readIDL(filename):
    with open(filename) as f:
        for line in f.readlines():
            image_name = re.search(r'".*"', line).group()
            re_label = re.search('\[.*\]', line).group()
            acc_re_label = re.split(r'[,\]\[]\s*',re_label)
            str_label = filter(lambda x: x != '',acc_re_label)
            label = map(int,map(round,map(float,str_label)))
            yield [image_name, label]
    print 'done'


#Define a main() function that prints a little greeting.
def main():
    for image, label in readIDL("test.idl"):
        print image, label





#This is standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
