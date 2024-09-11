import pandas as pd
import pyperclip
from datetime import datetime
from utilsHitting import *

# Load in pitching CSVs
metsAAAbrPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/BBrefMetsAAAPitchers.csv', encoding='latin-1')
metsAAASavantPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/BSMetsAAAPitchers.csv', encoding='latin-1')
leaguewideMilbTracker = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/milbTrackerCompletePitcherStats.csv', header=1)
leaguewideMilbTrackerAdv = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/milbTrackerCompleteAdvPitcherStats.csv', header=1, encoding='latin-1')
completeMetsAAAPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/CcompleteAAAMetsPitchingStats.csv', encoding='latin-1')

pitcherDefaultInfo = ['Player', 'Age', 'IP']
basicPitcherSlashLine = ['ERA', 'WHIP'] # , 'SO/W'

ctr = ['Rk', 'Rk.', 'Notes', 'Pitch %', 'Total']

# print(completeMetsAAAPitching[pitcherDefaultInfo + basicPitcherSlashLine])
print(leaguewideMilbTrackerAdv[pitcherDefaultInfo + basicPitcherSlashLine])
#print(leaguewideMilbTracker[leaguewideMilbTracker['Org'] == 'NYM'].sort_values(by='Player', ascending=False))