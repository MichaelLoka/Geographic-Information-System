# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

# 6- Using Search Cursor print the name, location & wikipedia for all airports which are major
arcpy.MakeFeatureLayer_management(airports, 'Airports_layer')
where_clause = "type = 'major'"
with arcpy.da.SearchCursor('Airports_layer', ['name', 'location', 'wikipedia', 'type'], where_clause) as airports_cursor:
    for x in airports_cursor:
        print(u"Airport name: {}".format(x[0]).encode('utf-8'))
        print(u"Location: {}".format(x[1]).encode('utf-8'))
        print(u"wikipedia: {}".format(x[2]).encode('utf-8'))
        print(x[3])
        print("")
