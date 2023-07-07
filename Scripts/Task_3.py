# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

# 3- Create a shapefile for roads in “Asia” continent + Print their number in Pycharm
arcpy.MakeFeatureLayer_management(Roads, 'Roads_Layer', """  "continent"='Asia'""")
arcpy.MakeFeatureLayer_management(countries, 'country_layer')
arcpy.SelectLayerByLocation_management('Roads_Layer', 'WITHIN', 'country_layer')
arcpy.FeatureClassToFeatureClass_conversion('Roads_Layer', output, 'Asia Roads')
# Get the count of the features in the shapefile
count = arcpy.GetCount_management('Roads_Layer')
print("Number of Roads In Asia = " + str(count))
