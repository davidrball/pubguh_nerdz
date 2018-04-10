# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:02:23 2018

@author: dball
"""

import numpy as np
from pubg_funcs import *
import matplotlib.pyplot as plt


myuser = 'davyjones128'
myregion = 'pc-na'

r_player = return_player_data(myuser,myregion)
match_list = return_recent_matches(r_player)

testmatch = match_list[0]

match_data = return_match_data('pc-na',testmatch)

tel_URL, tel_ID = return_tel_ID_URL(match_data)


tel_data = find_tel_data(tel_ID, tel_URL)
#tel_data = return_tel_data(tel_URL)
#save_tel_data(tel_data, tel_ID)

#let's define some functions for extracting info from telemetry
#e.g., we want to know how much damager a certain player did and with what weapons, let's first loop through telemetry and grab all info related to player


def attack_list(user):
    player_attack_list = []
    for i in tel_data:
        try:
            name = i['attacker']['name']
            if name == myuser:
                player_attack_list.append(i)
        except:
            pass
    return player_attack_list
    
my_attacklist = attack_list(myuser)