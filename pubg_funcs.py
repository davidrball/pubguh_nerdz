# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:32:39 2018

@author: dball
"""
import requests
import numpy as np

#a collection of functions that may be useful to call in later code

#a function for returning a list of match id's for a specific user
def return_recent_matches(user, region):
    match_list = []
    URL = "https://api.playbattlegrounds.com/shards/"+region+"/players?filter[playerNames]="+user
    #print(URL)
    header = {
    "Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NWI0NTNkMC0xOGRjLTAxMzYtNmZmMS01NWRjYjUxYTg4ZWIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTIyNjk4MzA4LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRhdnlqb25lcyIsInNjb3BlIjoiY29tbXVuaXR5IiwibGltaXQiOjEwfQ.lEZbaG1KelIytpxmhPGjGvCiegV5WY48QzloJIPo1xg",
    "Accept" : "application/vnd.api+json"}
    
    r = requests.get(URL,headers=header) #comment out when the IDE already has this info saved just for testing

    mydict = r.json()

    #print(mydict)
    #print(mydict.keys())
    #all info is under data key, which returns a list of length 1, which is a dictionary
    
    data = mydict['data'][0]
    #keys of this dictionary: type, links, attributes, relationship, id
    #type just gives the type of data, for instance, this is data from a specific player, so it returns player
    #link just returns the link to the URL pointing to this player's data, although with the account ID rather than name
    #attributes returns the player name, the time the data was pulled, patch version, region, etc.
    
    #relationships returns another dictionary
    relationships = data['relationships']
    match_data = relationships['matches']['data']
    
    #print(match_data) # a list of recent matches, each element in the list is a dictionary with id of match'
    for match in match_data:
        match_list.append(match['id'])
    return(match_list) #returns list of match ID's, which we should be able to query the matches to get actual info.
#e.g.,
myuser = "davyjones128"
myregion = "pc-na"
match_list = return_recent_matches(myuser,myregion)
print(len(match_list))
    
#return the ID for the telemtry from the request file
def return_tel_ID_URL(r):
    json = r.json()
    rtext = r.text
    data_rel = json['data']['relationships']
    tel_id = data_rel['assets']['data'][0]['id']
    #not sure what the 0 index does here, it's possible if you pull a list of matches into your json file that this index corresponds to individual matches?
    
    #now that we have the telemetry ID we can go find the URL in the rtext file    
    occurances = 0
    index_list = []
    index = 0
    skip = 10
    while index < len(rtext):
        tmpind = rtext[index:].find(tel_id)
        if tmpind != -1:
            occurances += 1
            index_list.append(tmpind+index)
            index = tmpind+index
        index += skip

#find there to be three instances, the first is just in the asset we find in data_rel
#2nd is followed by the URL
#third is just part of the URL
    
    url_scan = 250 #how far to go beyond the identifier to retrive the URL
    substr = rtext[index_list[1]:index_list[1]+url_scan]

    substr_start = substr.find("URL")
    substr_end = substr.find(".json")
    telemetry_URL = substr[substr_start+6:substr_end+5] #the +6 and 5 are just to clip off what should be standard formatting of spaces, colons, and "s
    print(telemetry_URL)#this is the link to the telemetry URL you want
    return telemetry_URL, tel_id

