# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

# 2- Create a shapefile for countries that have “military” airports + Print them in Pycharm
arcpy.MakeFeatureLayer_management(airports, 'Airports_layer', """ "type" IN ('military', 'major and military', 'mid and military', 'military mid') """)
arcpy.MakeFeatureLayer_management(countries, 'country_layer')
arcpy.SelectLayerByLocation_management('country_layer', 'INTERSECT', 'Airports_layer')
arcpy.FeatureClassToFeatureClass_conversion('country_layer', output, 'Countries_Militaries_Airports')
with arcpy.da.SearchCursor(r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output\Countries_Militaries_Airports.shp', ['NAME']) as cursor:
    for row in cursor:
        print(row[0])
