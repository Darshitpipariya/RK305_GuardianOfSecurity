import requests
import time
import pandas as pd

file = "Final{}.csv".format(time.strftime("%H_%d", time.localtime()))
try:
    api_url = "http://data.phishtank.com/data/%s/online-valid.csv" % (
        "71f70de52d2aa19f21e633f7ea0ece9c4c5a34b5074c6c9e8d5b58603d5a0ac6"
    )
    r = requests.get(api_url, allow_redirects=True)
    with open(file, "wb") as file:
        file.write(r.content)
    file1 = pd.read_csv(file)
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
df2.drop_duplicates(inplace=True)

final_file = pd.read_csv("Blacklist.csv")
before = len(final_file["url"])
df3 = df2.append(final_file)
df3.drop_duplicates(inplace=True)
df3.to_csv("Blacklist.csv", index=None)
print(len(df3["url"]) - before, " URL added")
print("No of URL in Dataset ", len(df3))
