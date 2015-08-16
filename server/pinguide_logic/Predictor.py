__author__ = 'viktor'

import Downloader

def predict_for(nickname, board_name):
    Downloader.fetch_images(nickname, board_name)
    dir = Downloader.get_dir(nickname, board_name)

