import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

la_url="http://www.iris.washington.edu/latin_am/evlist.phtml?region=mundo"
el_html = urlopen(la_url)
soup=BeautifulSoup(el_html)

"....."
data=[]

allrows =soup.find_all("tr")

for row in allrows:
    row_list = row.find_all('td')
    dataRow=[]
    
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)

df=pd.DataFrame(data)
"...."
header_list=[]
col_headers =soup.find_all('th')
for col in col_headers:
    header_list.append(col.text)

df.columns = header_list 
#df.to_csv('terremotos.csv')
print(df)
