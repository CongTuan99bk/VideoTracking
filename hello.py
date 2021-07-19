# import datetime
# from geopy.geocoders import Nominatim
# dt = datetime.datetime.today()
# datet = datetime.datetime.now()
# date = datet.strftime('%Y-%m-%d %H:%M:%S')
# # address = 'Ha Noi, Viet Nam'
# loc = Nominatim(user_agent="GetLoc")
# GetLoc = loc.geocode("Hanoi Vietnam")
# print(GetLoc.address)
# print(GetLoc.latitude, GetLoc.longitude)
# print(dt.month)
# import requests

# # Step 1) Find the public IP of the user. This is easier said that done, look into the library Netifaces if you're
# # interested in getting the public IP locally.
# # The GeoIP API I'm going to use here is 'https://geojs.io/' but any service offering similar JSON data will work.

# ip_request = requests.get('https://get.geojs.io/v1/ip.json')
# my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
# # print(my_ip)
# # Prints The IP string, ex: 198.975.33.4

# # Step 2) Look up the GeoIP information from a database for the user's ip

# geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
# geo_request = requests.get(geo_request_url)
# geo_data = geo_request.json()
# print(geo_data['latitude'])
# print(geo_data['longitude'])

from __future__ import print_function
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont
import cv2
# was: from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("arial.ttf", 18)
print(font)
im = Image.open("lena.jpg")
draw = ImageDraw.Draw(im)
text = "Lena's image"
draw.text((249,455), text, font=font, fill=(0, 0, 0))
# in PIL:
# print(font.getsize(text))
# mask = font.getmask(text)
print(ImageFont.getsize(text, font))
mask = ImageFont.getmask(text, font)
print(type(mask))
cv2.imshow("mask", mask)
im.show()