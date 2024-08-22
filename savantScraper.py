#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import argparse

def savantScraper(url, csv = False):
    '''
    Scrapes table from Baseball Savant minor league statcast search
    Parameters:
    ------------
    urL : Str
    string of the url to download the table from
    csv : Boolean
    boolean indicating weather or not to save the data as a csv
    '''
    clear = input("Clear?: ")
    if clear != "No":
        os.system('clear')
    else:
        pass

    if csv:
        fileName = input("Input CSV file name: ")
        fileName = "/Users/mj/Documents/Python/pyminorleague/csvs/" + fileName + ".csv"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find('table', id='search_results')
    df = pd.read_html(str(element))[0]
    df = df.drop(df.columns[1], axis=1)
    df = df.drop(df.columns[-1], axis=1)
    if csv: 
        df.to_csv(fileName, index=False, encoding='latin1')
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the magic number for a baseball team.")
    parser.add_argument('--csv', action='store_true', help="Set this flag to false")
    parser.add_argument("url", type=str, help="URL to parse")
    args = parser.parse_args()

    data = savantScraper(args.url, args.csv)
    print(data.head())