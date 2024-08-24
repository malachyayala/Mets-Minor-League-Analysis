import pandas as pd
import pyperclip
from datetime import datetime

minors_teams_dict = {
    "[ATH - AAA] Las Vegas Aviators": 400,
    "[ATL - AAA] Gwinnett Stripers": 431,
    "[AZ - AAA] Reno Aces": 2310,
    "[BAL - AAA] Norfolk Tides": 568,
    "[BOS - AAA] Worcester Red Sox": 533,
    "[CHC - AAA] Iowa Cubs": 451,
    "[CIN - AAA] Louisville Bats": 416,
    "[CIN - A] Daytona Tortugas": 450,
    "[CLE - AAA] Columbus Clippers": 445,
    "[COL - AAA] Albuquerque Isotopes": 342,
    "[CWS - AAA] Charlotte Knights": 494,
    "[DET - AAA] Toledo Mud Hens": 512,
    "[DET - A] Lakeland Flying Tigers": 570,
    "[HOU - AAA] Sugar Land Space Cowboys": 5434,
    "[KC - AAA] Omaha Storm Chasers": 541,
    "[LAA - AAA] Salt Lake Bees": 561,
    "[LAD - AAA] Oklahoma City Baseball Club": 238,
    "[LAD - AAA] Oklahoma City Dodgers": 238,
    "[MIA - AAA] Jacksonville Jumbo Shrimp": 564,
    "[MIA - A] Jupiter Hammerheads": 479,
    "[MIL - AAA] Nashville Sounds": 556,
    "[MIN - AAA] St. Paul Saints": 1960,
    "[MIN - A] Fort Myers Mighty Mussels": 509,
    "[NYM - AAA] Syracuse Mets": 552,
    "[NYM - A] St. Lucie Mets": 507,
    "[NYY - AAA] Scranton/Wilkes-Barre RailRiders": 531,
    "[NYY - A] Tampa Tarpons": 587,
    "[PHI - AAA] Lehigh Valley IronPigs": 1410,
    "[PHI - A] Clearwater Threshers": 566,
    "[PIT - AAA] Indianapolis Indians": 484,
    "[PIT - A] Bradenton Marauders": 3390,
    "[SD - AAA] El Paso Chihuahuas": 4904,
    "[SEA - AAA] Tacoma Rainiers": 529,
    "[SF - AAA] Sacramento River Cats": 105,
    "[STL - AAA] Memphis Redbirds": 235,
    "[STL - A] Palm Beach Cardinals": 279,
    "[TB - AAA] Durham Bulls": 234,
    "[TEX - AAA] Round Rock Express": 102,
    "[TOR - AAA] Buffalo Bisons": 422,
    "[TOR - A] Dunedin Blue Jays": 424,
    "[WSH - AAA] Rochester Red Wings": 534
}

# Load in CSV files
leaguewideAAAStatsDf = pd.read_csv('csvs/BSleaguewideAAAStats.csv', encoding='latin1')
metsAAAbballSavant = pd.read_csv('csvs/BSmetsAAAHittersStats.csv', encoding='latin1')
metsAAAbballRef = pd.read_csv('csvs/BBrefmetsAAAHitters.csv', encoding='latin1')
metsAAApbpSavant = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/BSmetsPitchByPitchHitters.csv', encoding='latin1')
completeMilbTrackerPitchers = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/milbTrackerCompletePitcherStats.csv', header=1)
metsAAApbpSavant = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/BSmetsPitchByPitchHitters.csv', encoding='latin1')
completeMetsAAAStats = pd.read_csv('/Users/mj/Documents/Python/pyminorleague/csvs/CcompleteAAAMetsStats.csv', encoding='latin1')

# Baseball Savant and Baseball Reference total stat Filters
defaultInfo = ['Player', 'Age', 'G', 'PA', 'AB']
basicStats = ['R', 'Hits', '1B', '2B', '3B', 'HR', 'RBI', 'SO', 'BB', 'BA', 'OBP', 'SLG', 'OPS', 'TB', 'GDP', 'HBP']
advancedStats = ['K%', 'BB%', 'Whiffs', 'Swings', 'xBA', 'xOBP', 'xSLG', 'wOBA', 'xwOBA', 'Barrels', 'BABIP', 'ISO', 'Whiff%', 'EV (MPH)', 'Adj. EV (MPH)' , 'LA (°)' , 'Dist (ft)', 'Hard Hit%', 'Barrel/BBE%', 'Barrel/PA%']
# LA (°)
slashLine = ['BA', 'OBP', 'SLG', 'OPS']
actualVsEx = ['BA', 'xBA', 'OBP', 'xOBP', 'SLG', 'xSLG', 'wOBA', 'xwOBA']
contactQuality = ['BIP', 'BABIP', 'Barrels', 'Hard Hit%', 'EV (MPH)', 'Adj. EV (MPH)', 'LA (ï¿½)', 'Dist (ft)', 'Barrel/BBE%', 'Barrel/PA%']
plateDiscipline = ['SO', 'K%', 'BB', 'BB%', 'Swings', 'Whiffs', 'Whiff%', 'Barrel/BBE%', 'Barrel/PA%', 'OBP', 'xOBP']
powerQuality = ['HR', 'SLG', 'xSLG', 'ISO', 'EV (MPH)', 'Adj. EV (MPH)', 'LA (ï¿½)', 'Dist (ft)', 'Hard Hit%']

# Baseball Savant pitch by pitch filters
hardContact = ['player_name', 'game_date', 'pitch_type', 'launch_angle', 'launch_speed', 'hit_location', 'hit_distance_sc', 'events', 'des']
pbpOuts = [
    'field_out',
    'double_play',
    'force_out',
    'grounded_into_double_play',
    'fielders_choice',
    'fielders_choice_out',
    'triple_play'
] # 'strikeout', 'strikeout_double_play'
def teamIdSearch(teamName):
    teamName = input("Enter team name: ")
    teamId = 0
    matching_teams = {team: team_id for team, team_id in minors_teams_dict.items() if teamName in team}
    for val in matching_teams.values():
        teamId = val
    
    print(teamId)
    return teamId

def affiliateSearch(teamId):
    matching_keys = [key for key, value in minors_teams_dict.items() if value == teamId]

    print(matching_keys)
    return(matching_keys)

def joinSavantBbref(savant, bballRef):
    '''
    Used to join a table scraped from Baseball Savant and Baseball Refence, both sorted in alphabetical order to players can be joined accordingly
    '''
    savant = savant.sort_values(by='Player')
    savant = savant.reset_index(drop=True)
    bballRef = bballRef.reset_index(drop=True)
    completeStats = savant.join(bballRef, lsuffix='', rsuffix="_right")

    columns_to_drop = [col for col in completeStats.columns if col.endswith('_right')]
    columns_to_drop.extend(['Rk', 'Rk.', 'Notes', 'Pitch %', 'Pitches', 'Total', 'Name', 'H'])
    completeStats = completeStats.drop(columns=columns_to_drop)

    completeStats.to_csv('csvs/CcompleteAAAMetsStats.csv', index = False, encoding='latin1')
    return completeStats

def calculateSavantStats(savantDf):
    savantDf.loc[:, 'TB'] = savantDf['1B'] + (2 * savantDf['2B'] + (3 * savantDf['3B']) + (4 * savantDf['HR']))
    savantDf.loc[:, 'RC'] = ((savantDf['Hits'] + savantDf['BB']) * savantDf['TB'])/(savantDf['AB'] + savantDf['BB'])

    return savantDf

def convertColumnsToNumeric(df, cols):
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def describeColumns(df, columns_to_convert):
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

    # Generate descriptive statistics for each specified column
    summary_df = pd.concat([df[col].describe() for col in columns_to_convert], axis=1)

    # Set the column names of the summary DataFrame to match the original column names
    summary_df.columns = columns_to_convert

    return summary_df

def analyzePbP(pbpDf, year, month, day):
    # rename first column
    pbpDf.columns.values[0] = 'pitch_type'

    # Create a specific date
    specific_date = datetime(year, month, day)

    # Format the date as YYYY-MM-DD
    formatted_date = specific_date.strftime('%Y-%m-%d')

    #pbpDf = pbpDf[pbpDf['game_date'] == formatted_date]

    pyperclip.copy(pbpDf.columns.tolist())

    # currently trying to filter by outs and see which pitch zone has the most outs
    final = pbpDf[['player_name', 'zone', 'launch_speed', 'pitch_type', 'events', 'description', 'game_date']].sort_values(by='launch_speed', ascending=False)
    print(final['zone'].value_counts())
    print(final['events'].unique())

completeMetsAAAStats['RC'] = ((completeMetsAAAStats['Hits'] + completeMetsAAAStats['BB']) * completeMetsAAAStats['TB'])/(completeMetsAAAStats['AB'] + completeMetsAAAStats['BB'])

# codify column: df['Team'].astype('category').cat.codes
#completeMetsAAAStats.plot(kind='bar', x='Player', y='HR', title='Home Runs by Player', legend=False)