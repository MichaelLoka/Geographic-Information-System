# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

#5- Create a shapefile for all Arabic cities using 2 methods ( Multiple Selections - If Condition )

# Multiple Selections Method
arabic_countries = ['Algeria', 'Bahrain', 'Comoros', 'Djibouti', 'Egypt', 'Iraq', 'Jordan', 'Kuwait',
                    'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia',
                    'Somalia', 'Sudan', 'Syria', 'Tunisia', 'United Arab Emirates', 'Yemen']
arcpy.MakeFeatureLayer_management(points, 'Points_Layer')
for i in arabic_countries:
    arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" ='{}' """.format(i))
    arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
    arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, '{}'.format(i))

# MAKE JUST ONE ShapeFile HAS ALL Arabic Countries
arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" IN {} """.format(tuple(arabic_countries)))
arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, 'Arabic cities')


# If Condition Method
arabic_countries = ['Algeria', 'Bahrain', 'Comoros', 'Djibouti', 'Egypt', 'Iraq', 'Jordan', 'Kuwait',
                    'Lebanon', 'Libya', 'Mauritania', 'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia',
                    'Somalia', 'Sudan', 'Syria', 'Tunisia', 'United Arab Emirates', 'Yemen']
arcpy.MakeFeatureLayer_management(points, 'Points_Layer')
arcpy.MakeFeatureLayer_management(countries, 'country_Layer')
with arcpy.da.SearchCursor('country_Layer', ['NAME']) as countries_cursor:
    for x in countries_cursor:
        if x[0] in arabic_countries:
            arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "NAME" ='{}' """.format(x[0]))
            arcpy.SelectLayerByLocation_management('Points_Layer', 'WITHIN', 'country_layer')
            arcpy.FeatureClassToFeatureClass_conversion('Points_Layer', output, '{}'.format(x[0]))

