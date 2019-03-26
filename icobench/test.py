

import scrapy
import os
from icobench.items import *






if __name__ == '__main__':
    icobench = IcobenchItem()
    print(icobench)
    x='project name'
    x=x.replace(' ','_')
    icobench[x]=123
    print(icobench)