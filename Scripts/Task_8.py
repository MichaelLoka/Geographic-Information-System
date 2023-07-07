import arcpy

arcpy.env.overwriteOutput = True

Roads = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
pop_number = arcpy.GetParameterAsText(3)

total_count = 0
created_count = 0

arcpy.MakeFeatureLayer_management(Roads, 'Roads_layer')
arcpy.MakeFeatureLayer_management(countries, 'Countries_layer')
where_clause = "CONTINENT = 'Africa' "

with arcpy.da.SearchCursor('Countries_layer', ['SOVEREIGNT', 'INCOME_GRP', 'FID', 'POP_EST'], where_clause) as cursor:
    for x in cursor:
        total_count += 1
        if x[3] > float(pop_number):
            created_count += 1
            arcpy.MakeFeatureLayer_management(countries, 'Countries_layer', """ "FID"={} """.format(x[2]))
            arcpy.SelectLayerByLocation_management('Roads_layer', 'WITHIN', 'Countries_layer')
            formatted_output_name = x[0].replace('(','_').replace(')','_')
            formatted_income_group = x[1].replace(' ', '_')
            output_name = 'Roads_in_{}_{}.shp'.format(formatted_output_name, formatted_income_group)
            # Create a new shapefile for the selected roads
            output_path = '{}/{}'.format(output, output_name)
            arcpy.FeatureClassToFeatureClass_conversion('Roads_layer', output, output_name)
            print('Successfully converted {} \n'.format(formatted_output_name))
            arcpy.AddMessage('Successfully converted {} \n'.format(formatted_output_name))

        else:
            print("{} didn't meet the criteria".format(x[0].encode('utf-8')))
            arcpy.AddMessage("{} didn't meet the criteria".format(x[0].encode('utf-8')))

print("\n")
print('Finished')
arcpy.AddMessage('Finished!!!')
print('{0} met the criteria out of {1} countries'.format(created_count, total_count))
arcpy.AddMessage('{0} met the criteria out of {1} countries'.format(created_count, total_count))