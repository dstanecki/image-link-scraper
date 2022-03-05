import urllib
import requests
from pandas import *
import pandas as pd
import urllib.request


if __name__ == '__main__':
    csv_name = input("Enter the spreadsheet file name:\n")
    data = read_csv(csv_name)
    images_unfiltered = data["Featured Image"].tolist()  # Puts all cell values in "Featured Image" column into a list
    images = [x for x in images_unfiltered if pd.isnull(x) == False]  # Filters out blank cell values. Remaining values should all be direct URL links to images 
    scrape()
    
    
# Iterates over 'images' list and saves images to a local directory
def scrape():
    for url in images:
        try:
            file_name = '/Users/Library/Desktop/eNewsletter/' + url.rsplit('/', 1)[-1] # Saves images to eNewsletter folder, 
            # file is named after the text that follows the last slash in the url
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
            with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
        except Exception as exc:
            print(f"Exception occurred while downloading image from url {url} {str(exc)}")
