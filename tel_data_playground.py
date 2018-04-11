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

testmatch = match_list[2]

match_data = return_match_data('pc-na',testmatch)

tel_URL, tel_ID = return_tel_ID_URL(match_data)


tel_data = find_tel_data(tel_ID, tel_URL).json()
#tel_data = return_tel_data(tel_URL)
#save_tel_data(tel_data, tel_ID)

#let's define some functions for extracting info from telemetry
#e.g., we want to know how much damager a certain player did and with what weapons, let's first loop through telemetry and grab all info related to player

#defining a mapping between the colloquial gun names and the in game names w/ lots of letters

#gun_map = {'WeapAK47_C':'AK'}

'''
def kill_list(user):
    player_kill_list = []
    for i in tel_data:
        try:
            name = i['attacker']['name']
            if name == myuser:
                player_attack_list.append(i)
        except:
            pass
    return player_attack_list
'''
'''
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
'''


def attack_list(user, tel_data):   
    player_attack_list = []
    for i in tel_data:
        if i['_T'] == 'LogPlayerAttack':
           # print('triggered')
            if i['attacker']['name'] == user:
                print('triggered')
                player_attack_list.append(i)
    return player_attack_list

def damage_list(user, tel_data):    #given a user, returns all the instances of damage they did during a single game
    player_attack_list = []
    for i in tel_data:
        if i['_T'] == 'LogPlayerTakeDamage':
           # print('triggered')
            if i['attacker']['name'] == user:
                #print('triggered')
                player_attack_list.append(i)
    return player_attack_list

my_damage_list = damage_list(myuser, tel_data)
'''
my_attacklist = attack_list(myuser)

for attack in my_attacklist:
    print(attack['_T'])
'''
'''
my_damage_list = []
damage_dict = {}
for attack in my_attacklist:
    if attack['_T'] == 'LogPlayerTakeDamage':
        my_damage_list.append(attack)
#now loop through instances of giving damage and assign them to different weapons
'''

def gun_damage(my_damage_list):
    damage_dict = {}
    for damage in my_damage_list:
        weapon = damage['damageCauserName']
        if weapon in damage_dict.keys():
            damage_dict[weapon] += damage['damage']
            #print('updated damage for ', weapon)
        else:
            damage_dict[weapon] = damage['damage']
            #print('new weapon ', weapon, damage['damage'])
    return damage_dict
gun_damage_dict = gun_damage(my_damage_list)
