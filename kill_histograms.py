# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:26:37 2018

@author: davidrball
"""

#want to make a histogram of kills

import numpy as np
from pubg_funcs import *
import matplotlib.pyplot as plt


myuser = 'davyjones128'
myregion = 'pc-na'

r_player = return_player_data(myuser,myregion)
match_list = return_recent_matches(r_player)

#print(match_list)

#mydata = find_match_data('pc-na',match_list[0]).json()

#data_included = mydata['included'] # a list of the teams / players


kill_list = []
num_matches = 5

for i in range(0,num_matches):
    mydata = find_match_data('pc-na',match_list[i]).json()
    data_included = mydata['included']
    for data in data_included:
        if data['type']=='participant':
            kills = data['attributes']['stats']['kills']
            kill_list.append(kills)
kill_array = np.array(kill_list)
plt.hist(kill_array,bins=20)