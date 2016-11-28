#!/home/ch/anaconda/bin/python
# -*- coding: utf-8 -*-
#Author: Chen Hao

import sys
sys.path.append('/usr/lib/python2.7/dist-packages/')
import cv2



#Define a main() function that prints a little greeting.
def main():
    img = cv2.imread('./60091.jpg')
    print img.shape

#This is standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()