import arcpy

points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Data\ne_10m_populated_places.shp'
Output_Points = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output\output_shapefile.shp'
arcpy.CopyFeatures_management(points, Output_Points)

field_list = arcpy.ListFields(Output_Points)
# print field_list
list_field = []

for x in field_list:
    # print x.name
    # print x.type
    if x.type != 'String':
        list_field.append(x.name)

for field in list_field:
    with arcpy.da.UpdateCursor(Output_Points, [field]) as city_cursor:
        for x in city_cursor:
            if x[0] == ' ' or x[0] == 0 or x[0] == '':
                x[0] = 1.0111111
                city_cursor.updateRow(x)

print ('Mission Done Son of b!tch')
