#!/usr/bin/python3

key = 's67wt459muuhe5c9mus424v3'

from Data import Data
retriever = Data(key)

stageid = 432291
#prettyxml = retreiver.getStage(stageid, key)
competitorid = 7135
prettyxml = retriever.getCompetitor(competitorid, key)
