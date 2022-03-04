import urllib
from pandas import *
import pandas as pd
import urllib.request
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


def scrape():
    csv_name = input("Enter the spreadsheet file name:\n") # change this to method parameter^
    data = read_csv(csv_name)
    images_unfiltered = data["Featured Image"].tolist()
    images = [x for x in images_unfiltered if pd.isnull(x) == False]
    count = 1
    for url in images:
        try:
            file_name = '/Users/Library/Desktop/Test/' + url.rsplit('/', 1)[-1] # names the file whatever is after
            # the final slash in the URL
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
            with urllib.request.urlopen(req) as response, open(file_name, 'wb') as out_file:
                data = response.read()  # a `bytes` object
                out_file.write(data)
            count += 1
        except Exception as exc:
            print(f"Exception occurred while downloading image from url {url} {str(exc)}")
    # still want to use Mailchimp API to add files to File Manager, replicate campaign

def upload():
    try:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": "YOUR_API_KEY",
            "server": "YOUR_SERVER_PREFIX"
        })
        response = client.fileManager.upload({"name": "name", "file_data": "file_data"})
        print(response)
    except ApiClientError as error:
        print("Error: {}".format(error.text))

if __name__ == '__main__':
    scrape()
