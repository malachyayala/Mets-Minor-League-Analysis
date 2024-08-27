#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import argparse

def bballRefScraper(url, tableName, csv = False):
    '''
    Scrapes a table from baseball reference but unfortunately only works for tables that aren't lazy loaded (I believe.) Will be building one to scrape all tables using Selenium
    Parameters:
    ------------
    urL : Str
    string of the url to download the table from
    tableName : Str
    string representing the name of the table to scrape.
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
    soup = BeautifulSoup(response.content, 'lxml')
    element = soup.find('table', id=tableName)
    df = pd.read_html(str(element))[0]
    if csv: 
        df.to_csv(fileName, index=False, encoding='utf8')
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the magic number for a baseball team.")
    parser.add_argument('--csv', action = 'store_true', help = "Set this flag to false")
    parser.add_argument('tableName', type = str, help = "Table name to parse")
    parser.add_argument("url", type = str, help = "URL to parse")
    args = parser.parse_args()

    data = bballRefScraper(args.url, args.tableName, args.csv)
    print(data.head())