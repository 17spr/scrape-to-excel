from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# function for saving data to csv file
f = open('data_output.csv', 'w', newline = '')
writer = csv.writer(f)

# storing the website url
url = "https://en.wikipedia.org/wiki/Global_music_industry_market_share_data"
# function for opening the url
html = urlopen(url)

# function for parsing the html
soup = BeautifulSoup(html, 'lxml')

# navigating to the desired data contained in the tbody tag
tbody = soup('table', {'class': 'wikitable plainrowheaders sortable'})[0].find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    # strip html tags and retrieve only text of data values
    cols = [ele.text.strip() for ele in cols]
    # write to csv file
    writer.writerow(cols)
    print(cols)
