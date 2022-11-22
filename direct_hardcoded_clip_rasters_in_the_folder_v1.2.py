import os
import os, fnmatch

# Directly define the input, output raster names and shapefile name for the required Raster and shape for clipping
inputraster = r'H:/Solar_Suitability_Mapping_v1_3_September_2022/Scripts_codes/Python/test_0/roads_distance_90_signed16.tif'
outputraster = r'H:/Solar_Suitability_Mapping_v1_3_September_2022/Scripts_codes/Python/test_1/testclip_roads_distance_90_signed16.tif'
shapefile = r'"H:/Solar_Suitability_Mapping_v1_3_September_2022/Boundaries/Africa_Parts/Parts_Stage_2/s2_part_1.shp"'

# gdal command
cmd = 'gdalwarp -q -cutline %s -crop_to_cutline %s %s' % (shapefile, inputraster, outputraster)
os.system(cmd)