import requests
import time
import pandas as pd
import os
file = "Final.csv"
try:
    api_url = "http://data.phishtank.com/data/%s/online-valid.csv" % (
        "71f70de52d2aa19f21e633f7ea0ece9c4c5a34b5074c6c9e8d5b58603d5a0ac6"
    )
    r = requests.get(api_url, allow_redirects=True)
    with open(file, "wb") as file1:
        file1.write(r.content)
    file1 = pd.read_csv(file)
except:
    pass
try:
    df1 = pd.DataFrame()
    df1["url"] = file1["url"]
except:
    file = "phish1.csv"
    file1 = pd.read_csv(file)
    df1 = pd.DataFrame()
    df1["url"] = file1["url"]
    
open_phis = "https://openphish.com/feed.txt"
r = requests.get(open_phis, allow_redirects=True)
url_list = []
for i in r.content.decode().split():
    url_list.append(i.strip())
df2 = pd.DataFrame()
df2["url"] = url_list
df2 = df2.append(df1)
df2.drop_duplicates(subset=['url'],inplace=True)

#file = "Final{}.csv".format(time.strftime("%H_%d", time.localtime()))
df2.to_csv("new_file.csv",index=None)
new=pd.read_csv("new_file.csv")
old = pd.read_csv("Blacklist.csv")


li=list(new['url'])
a=old
a=a.append(new)
a.to_csv(r"merge.csv",index=None)
b=pd.read_csv(r"merge.csv")
li=list(b.duplicated())
du=[]
for i in range(len(li)):
    if li[i]==True:
        du.append(b['url'][i])
new_data=[]
for i in list(new['url']):
    if i not in du:
        new_data.append(i)
data_fr=pd.DataFrame()
data_fr['url']=new_data
data_fr.to_csv(r"today_url.csv",index=None)
b.drop_duplicates(subset=['url'],inplace=True)
b.to_csv(r"Blacklist.csv",index=None)
os.remove("Final.csv")
os.remove('merge.csv')
os.remove("new_file.csv")
