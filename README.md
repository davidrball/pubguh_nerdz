# pubguh_nerdz

hey nerdz,

since it's in the very early stages of the open beta, I've just been trying to develop really basic tools for extracting useful information from the data structures they give you (which I've never used before so I'm probably doing things in a sub-optimal way).  To this end, I've mostly been adding functions to pubg_funcs.py so they can be used later to facilitate writing actual analysis code.

Right now you can only download data from PUBG 10 times per minute, which means if you're interested in, e.g., a player's stats over more than 10 games, you're hosed.  

Furthermore, they aren't releasing individual player statistics (total kills, deaths, etc.), so the only way to get player stats is to loop through the matches you've played and grab the data from those.  This makes getting the total stats for a player really clunky, since you can't get all the matches at once (presuming you've played more than 10 games...)

However, the developers said in their roadmap that one of the next things they're oging to be adding are player stats, so I don't think writing our own routines for extracting these from matches is worth it.

Where things get really interesting is the "telemetry" data, which are a few gigs per file that have detailed match data (effectively all the info that's in a replay).  I haven't played with these yet, but I think this would be a good place to start, as the player stats are going to be built in from pubg's end soon anyways.