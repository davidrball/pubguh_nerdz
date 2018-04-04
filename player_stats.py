# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:27:31 2018

@author: dball
"""


import numpy as np
from pubg_funcs import return_player_data, return_recent_matches, return_match_data

#let's loop through all matches from a given player, and look at basic stats.  Kills, wins, damage, etc.

myuser = 'davyjones128'
myregion = 'pc-na'

r_player = return_player_data(myuser,myregion)
match_list = return_recent_matches(r_player)
#print(match_list)

#loop through matches and grab data

data_list = []
numgames = 5
for i in range(0,numgames): #for a subset of games
#for i in range(len(match_list)): # for all games
    match_id = match_list[i]
    tmpr = return_match_data('pc-na',match_id).json()
    tmpr = tmpr['included']
    data_list.append(tmpr)
#now we have list of json files which contain the details from matches.
#need to loop through these, find entry that contains info about player you want
#quickly running into limit issues, since we're grabbing info from lots of matches
#a developer in the discord says that they're planning onimplementing a player profile that gives lifetime stats
    
kill_list = []
for i in range(len(data_list)):
    gamedata = data_list[i]
    for j in range(len(gamedata)):
        #this will be looping through both teams and players, for now we just want players
        if gamedata[j]['type'] == 'participant':
            playername = gamedata[j]['attributes']['stats']['name'] #extract name of player
            if playername == myuser: #probably more efficient to do this in term of player id rather than name, but oh well
                kill_list.append(gamedata[j]['attributes']['stats']['kills'])
        else:
            pass