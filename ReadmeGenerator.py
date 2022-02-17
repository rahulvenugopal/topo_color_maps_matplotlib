# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:43:32 2022
- Automate generating readme for topo colormaps
@author: Rahul Venugopal
"""
from glob import glob

list = glob('*.png')

for items in list:
    print(items[:-4])
    filename = 'https://raw.githubusercontent.com/rahulvenugopal/topo_color_maps_matplotlib/main/maps/'
    print('![]('+filename+items+')')
    print('\n')

