# search torrent online

import urllib
import re
import os
import requests

# get the torrent file
def get_torrent_furlopenile(torrent_name):
    # get the torrent file
    torrent_file = urllib.request.urlopen("https://torrentz2.eu/search?f=" + torrent_name)
    # read the torrent file
    torrent_file = torrent_file.read()
    # get the magnet link
    magnet_link = re.findall(r'magnet:\?xt=urn:btih:[a-zA-Z0-9]*', torrent_file)
    # return the magnet link
    return magnet_link

# download the torrent file
def download_torrent_file(torrent_name):
    # get the magnet link
    magnet_link = get_torrent_furlopenile(torrent_name)
    # download the torrent file
    os.system("transmission-remote -a " + magnet_link[0])

# search torrent online
def search_torrent_online(torrent_name):
    # download the torrent file
    download_torrent_file(torrent_name)

# input the torrent name to search
torrent_name = input("Enter the torrent name to search: ")
# search torrent online
print("Searching torrent online...")
search_torrent_online(torrent_name)


