from exif import Image
from geopy.geocoders import Nominatim

def dms_to_dd(gps_coords, gps_coords_ref):
    d, m, s =  gps_coords
    dd = d + m / 60 + s / 3600
    if gps_coords_ref.upper() in ('S', 'W'):
        return -dd
    elif gps_coords_ref.upper() in ('N', 'E'):
        return dd
    else:
        raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))
        
def location(img_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
        print(src.name, img)

        if img.has_exif:
            info = f" has the EXIF {img.exif_version}"
        else:
            info = "does not contain any EXIF information"
            print(f"Image {src.name}: {info}")

        #Read again photo with exif info
        img.list_all()

        my_image = img
        print(dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref))
        print(dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref))
        lat = dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref)
        long = dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref)

        # calling the nominatim tool
        geoLoc = Nominatim(user_agent="locfrompic")
        
        # passing the coordinates
        locname = geoLoc.reverse((lat,long), language='en').raw
        
        # printing the address/location name
        print(locname)
        return locname

def main():
    location("./static/uploads/IMG_8765.jpeg")

if __name__ == "__main__":
    main()