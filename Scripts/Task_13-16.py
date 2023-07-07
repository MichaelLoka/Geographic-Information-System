import os
from PIL import Image, ExifTags
import arcpy
arcpy.env.overwriteOutput = True
#task 13
print("Task 13: ")
img_folder = r"E:\8th Semester\GIS\GIS Application\Images"
img_content = os.listdir(img_folder)
for image in img_content:
    #print image
    full_path = os.path.join(img_folder, image)
    print(full_path)
#task 14
for image in img_content:
    print("Task 14: ")
    full_path = os.path.join(img_folder, image)
    pil_img = Image.open(full_path)

    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}
    print(exif)
#task 15
    print("Task 15: ")
    gps_all={}
    try:
        for key in exif['GPSInfo'].keys():
            decoded_value = ExifTags.GPSTAGS.get(key)
            gps_all[decoded_value]=exif['GPSInfo'][key]
            print("{0}: {1}".format(decoded_value, gps_all[decoded_value]))
    except:
        print("This is image has no GPS info in it{}".format(full_path))
        pass
#task 16
    print("Task 16: ")
    long_ref = gps_all.get('GPSLongitudeRef')
    longitude =gps_all.get('GPSLongitude')
    lat_ref = gps_all.get('GPSLatitudeRef')
    latitude = gps_all.get('GPSLatitude')
    print(long_ref,"  ",longitude)
    print(lat_ref,"  ",latitude)
    print('-'*50)