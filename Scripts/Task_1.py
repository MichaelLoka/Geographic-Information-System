# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

# 1- List all data we’re working with and show them on ArcMap
arcpy.env.workspace = r'E:\8th Semester\GIS\GIS Application\Data'
feature_list = arcpy.ListFeatureClasses()
print (feature_list)
