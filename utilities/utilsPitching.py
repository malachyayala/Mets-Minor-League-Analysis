import pandas as pd
import pyperclip
from datetime import datetime
from utilsHitting import *

metsAAAbrPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/BBrefMetsAAAPitchers.csv', encoding='latin1')
metsAAASavantPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/BSMetsAAAPitchers.csv', encoding='latin1')
leaguewideMilbTracker = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/milbTrackerCompletePitcherStats.csv', header=1)
completeMetsAAAPitching = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/pitching/CcompleteAAAMetsPitchingStats.csv', encoding='latin1')


ctr = ['Rk', 'Rk.', 'Notes', 'Pitch %', 'Total']

print(completeMetsAAAPitching[['Player', 'Age']])