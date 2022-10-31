from exif import Image
from geopy.geocoders import Nominatim

img_path = 'ELcat.jpeg'
with open(img_path, 'rb') as src:
    img = Image(src)
    print (src.name, img)

if img.has_exif:
    info = f" has the EXIF {img.exif_version}"
else:
    info = "does not contain any EXIF information"
print(f"Image {src.name}: {info}")

#Read again photo with exif info
with open(img_path, "rb") as src:
    img = Image(src)
img.list_all()

def dms_	to_dd(gps_coords, gps_coords_ref):
    d, m, s =  gps_coords
    dd = d + m / 60 + s / 3600
    if gps_coords_ref.upper() in ('S', 'W'):
        return -dd
    elif gps_coords_ref.upper() in ('N', 'E'):
        return dd
    else:
        raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))

with open('airportdtw.jpeg', 'rb') as image_file:
    my_image = Image(image_file)

    # gps_latitude = (32.0, 37.0, 37.15)
    # gps_longitude = (116.0, 30.0, 37.0)
    # 
    # gps_latitude_ref = 'N'
    # gps_longitude_ref = 'W'

with open('ELcat.jpeg', 'rb') as image_file:
    my_image = Image(image_file)
    print(dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref))
    print(dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref))
lat = dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref)
longg= dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref)
locname = geoLoc.reverse((lat,longg), language='en').raw
 
# printing the address/location name
locname