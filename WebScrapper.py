"""
You need to Install 2 Library to run this Web Scrapper

1. $ pip3 install requests
2. $ pip3 install beautifulsoup4
"""

from bs4 import BeautifulSoup
import requests
import csv

# Base URL - To Fetch Data
baseURL = "https://basantmandal.github.io/"

# Lets Get Data & Store it in Object
html_content        = requests.get(baseURL).text

# Parse HTML Code With Beautiful Soup
soup                = BeautifulSoup(html_content, "html.parser") 

# Lets Get Title Data
page_title          = soup.title.string

# Lets Get Meta Data
page_description    = "";
page_og_title       = "";

print(" ================ Scrapping Started ============= \n")

print(" > Searching Meta Information Started..");
# Search in Meta
for meta in soup.findAll("meta"):
    meta_name = meta.get('name', '').lower()
    meta_property = meta.get('property', '').lower()
    meta_content = meta.get("content", '')

    # I want to collect the WebSite Title, Descrition & Few OG Data if Exists, You can customize it as per yur needs.
    page_description = '';
    page_og_title = '';
    page_twitter_url = '';
    page_keyword = '';

    # Uncomment for Debug Purpose
    # print("Meta Name :- " + str(meta_name) + " = " +  str(meta_content) if meta_name else "")

    # If Data found assign it
    if meta_name == 'description' or meta_property == "description":
        page_description = meta['content']

    if meta_name == 'keyword' or meta_property == "keyword":
        page_keyword = meta['content']

    if meta_name == 'og:title' or meta_property == "og:title":
        page_og_title = meta['content']

    if meta_property == 'twitter:url':
        page_twitter_url = meta['content']

# Once Data is Collected, Lets Write in CSV (Append Mode)

print(" > Searching Meta Information Completed..");

# CSV File Name
csvFileName = "websiteData.csv";

print(" > Writing Data on CSV File Started..");

# Open & Appends CSV File
with open(csvFileName, 'a') as csv_file_object:
    cwriter = csv.writer(csv_file_object, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    # Header - Top Row 
    cwriter.writerow(['Website Title', 'Website Description', 'Keyword', 'Page Og Title', 'Page Twitter URL'])
    cwriter.writerow([page_title, page_description, page_keyword, page_og_title, page_twitter_url])
#ends

print(" > Writing Data on CSV File Completed.. \n");
print(" ================ Scrapping Completed ============= ")
