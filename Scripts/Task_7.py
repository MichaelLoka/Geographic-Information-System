# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
countries = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_admin_0_countries.shp '
points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
airports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_airports.shp'
Roads = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_roads.shp'
Ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_ports.shp'
output = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output'

# 7- Using Search Cursor create shapefiles for roads in countries based on (FID & Sovereignty)
# condition that region is “Africa” & population > 25 million Let files names be in the format
# of “Roads_in_CountryName_CountryIncome”
arcpy.MakeFeatureLayer_management(Roads, 'Roads_layer')
arcpy.MakeFeatureLayer_management(countries, 'Countries_layer')
where_clause = "CONTINENT = 'Africa' AND POP_EST > 25000000"
with arcpy.da.SearchCursor('Countries_layer', ['SOVEREIGNT', 'INCOME_GRP', 'FID'], where_clause) as cursor:
    for x in cursor:
        arcpy.MakeFeatureLayer_management(countries, 'Countries_layer', """ "FID"={} """.format(x[2]))
        arcpy.SelectLayerByLocation_management('Roads_layer', 'WITHIN', 'Countries_layer')
        formatted_output_name = x[0].replace('(','_').replace(')','_')
        formatted_income_group = x[1].replace(' ', '_')
        output_name = 'Roads_in_{}_{}.shp'.format(formatted_output_name, formatted_income_group)
        # Create a new shapefile for the selected roads
        output_path = '{}/{}'.format(output, output_name)
        arcpy.FeatureClassToFeatureClass_conversion('Roads_layer', output, output_name)
