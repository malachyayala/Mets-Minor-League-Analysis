#!/usr/bin/env python3
import argparse
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapeMilbTracker(url, pageCount, csv = False):
    '''
    Scrapes table from Milbtracker.com
    Parameters:
    ------------
    urL : Str
    string of the url to download the table from
    pageCount : int
    integer representing the number of pages a table has
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

    df_list = []

    # Loop through the paginated pages
    for page in range(1, pageCount):  # Replace total_pages with the number of pages or use a while loop
        url = url + f'&page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use pandas to read the table directly from the HTML
        tables = pd.read_html(str(soup), header=1)
    
        # Assuming the table you need is the first one on the page
        df = tables[0]
    
        # Append the DataFrame to the list
        df_list.append(df)

    # Concatenate all the DataFrames in the list into one DataFrame
    final_df = pd.concat(df_list, ignore_index=True)

    # Now you can save the combined DataFrame or process it further
    if csv: 
        final_df.to_csv(fileName, index=False, encoding='latin1')
    return final_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the magic number for a baseball team.")
    parser.add_argument('--csv', action='store_true', help="Set this flag to false")
    parser.add_argument("--pageCount", type=int, help="Number of pages to scrape", default=10)  # New integer argument
    parser.add_argument("url", type=str, help="URL to parse")

    args = parser.parse_args()

    data = scrapeMilbTracker(args.url, args.pageCount, args.csv)
    print(data.head())