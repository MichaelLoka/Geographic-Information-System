import arcpy

#arcpy.env.overwriteOutput = True

countries = arcpy.GetParameterAsText(0)
Value = arcpy.GetParameterAsText(1)

Output_Points = r'E:\8th Semester\GIS\GIS Application\Output\output_shapefile.shp'

arcpy.CopyFeatures_management(countries, Output_Points)

with arcpy.da.UpdateCursor(Output_Points, ['FID','NAME','POP_EST','POP_YEAR']) as countres_cursor:
    for x in countres_cursor:
        if x[3] < 2019:
            x[2] = Value
            country_name = x[1].encode('utf-8')
            arcpy.AddMessage("Country {0} is updated".format(country_name))
            countres_cursor.updateRow(x)
