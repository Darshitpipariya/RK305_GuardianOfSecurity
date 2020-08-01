import requests
def unshort(url):
    my_url=url
    try:
        if not(my_url.startswith("http") or my_url.startswith("https")):
            my_url="https://"+my_url
        r=requests.get(my_url)
        new_url=r.url
        final_url=new_url[new_url.rfind("http"):]
        return final_url
    except:
        return url
if __name__=="__main__":
    
    url=input("Enter Url : ")
    unshort_url=unshort(url)
    print(unshort_url)
