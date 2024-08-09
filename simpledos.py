#Yes, i already know, is a simple ping test or a simple DOS | this code can't even server down a simple site

import requests

target = "https://" + input("Paste a site address: ")

print(target + " | ")

while True:
    r = requests.get(target)

    print("ping : " + str(r.status_code))
