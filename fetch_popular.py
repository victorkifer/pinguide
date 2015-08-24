from bs4 import BeautifulSoup
import time
import urllib
import urllib2
import json
import urllib
import time
##########################################################
def fetch_images(link) : 
        filename = link[link.rindex("/"):]
        with open("popular/" + filename, 'w') as f:
            f.write(fetch_file(link))   
##########################################################
def fetch_file(link) :
        url = link
        headers = {"X-Requested-With" : "XMLHttpRequest"}
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page
##########################################################
def parse_json(url) : 
    print url
    data = fetch_file(url)
#    print data
    vals = json.loads(data)

    bookmarks = vals["resource"]["options"]["bookmarks"]
    
    for val in vals["resource_response"]["data"] : 
        if "id" in val :
            url = val["images"]["orig"]["url"]            
            print url
            fetch_images(url)
            
    return bookmarks
##########################################################
def fetch_popular(cursor = None) :
    if cursor is None : 
        cursor = parse_json('https://www.pinterest.com/resource/CategoryFeedResource/get/?source_url=%2Fcategories%2Fpopular%2F&data=%7B%22options%22%3A%7B%22feed%22%3A%22popular%22%2C%22low_price%22%3Anull%2C%22high_price%22%3Anull%2C%22is_category_feed%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D')        
    else : 
        time.sleep(0.1)
        books = urllib.quote(json.dumps(cursor))
        cursor = parse_json('https://www.pinterest.com/resource/CategoryFeedResource/get/?source_url=%2Fcategories%2Fpopular%2F&data=%7B%22options%22%3A%7B%22feed%22%3A%22popular%22%2C%22low_price%22%3Anull%2C%22bookmarks%22%3A' + books + '%2C%22high_price%22%3Anull%2C%22is_category_feed%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D')
    return cursor
##########################################################
def fetch_all_popular(n = 10) :
    cursor = None
    for x in range(0, n):
        cursor = fetch_popular(cursor)        
##########################################################
fetch_all_popular()
