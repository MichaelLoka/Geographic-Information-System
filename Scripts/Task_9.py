import arcpy

ports = arcpy.GetParameterAsText(0)
website = arcpy.GetParameterAsText(1)
output_ports = r'D:\ASU FCIS 2023\Year 4\Semester 2\5. Geographic Information Systems\Project\GIS Application\Output\output_shapefile.shp'

# Copy input ports shapefile to output ports shapefile
arcpy.CopyFeatures_management(ports, output_ports)


# Modify website field in output ports shapefile
with arcpy.da.UpdateCursor(output_ports, ['website']) as website_cursor:
    for x in website_cursor:
        if x[0] == " ":
            x[0] = website
            website_cursor.updateRow(x)
            print("New value:", x[0])
            arcpy.AddMessage("New Value: {}".format(x[0]))
        else:
            arcpy.AddMessage("Same Value: {}".format(x[0]))



