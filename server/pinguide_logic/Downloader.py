__author__ = 'victor'

import urllib
import urllib2
from bs4 import BeautifulSoup
import time
import os
import shutil
import ImageProcessor

from pinguide_config import FOLDER_TMP

##########################################################
def __fetch_file(link) :
  # user_agent  = 'curl/7.29.0'
  # host = 'www.pinterest.com'
  # accept = '*/*'

  url = link
  # user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
  # values = {}
  # headers = {"User-Agent" : user_agent, "Host" : host, "Accept" : accept} #{'User-Agent' : user_agent }
  # headers = {} #{'User-Agent' : user_agent }
  # data = urllib.urlencode(values)
  req = urllib2.Request(url) #, data, headers)
  response = urllib2.urlopen(req)
  the_page = response.read()
  return the_page

#########################################################
def get_link(nickname, board_name):
  return 'https://www.pinterest.com/' + nickname + '/' + board_name + '/'

#########################################################
def get_dir(nickname, board_name):
  return FOLDER_TMP + '/' + nickname + '/' + board_name + '/'

##########################################################
def ensure_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

##########################################################
def fetch_images(nickname, board_name):
  url = get_link(nickname, board_name)
  dir = get_dir(nickname, board_name)
  ensure_dir(dir)

  html_code = __fetch_file(url)
  soup = BeautifulSoup(html_code, 'html.parser')

  for link in soup.find_all('img'):
    if not link.has_attr("class"):
      continue
    if not "pinImg" in link["class"]:
      continue
    time.sleep(0.1)
    link = link["src"]
    filename = link[link.rindex("/"):]
    with open(dir + filename, 'wb+') as f:
      f.write(__fetch_file(link))

    ImageProcessor.resize_and_crop(
      dir + filename,
      dir + filename,
      (256, 256),
      crop_type='middle'
    )


##########################################################
def remove_download(nickname, board_name):
  dir = FOLDER_TMP + '/' + nickname + '/'
  shutil.rmtree(dir, True)

# fetch_images('https://www.pinterest.com/nick_goodey/under-the-sea/')