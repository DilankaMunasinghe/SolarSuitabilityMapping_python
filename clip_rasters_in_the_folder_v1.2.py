# This Script could be used to clip multiple raster files (GeoTIFF or .tif) to the shapes of multiple shapefiles and produce corresponding outputs according to the names of the Rasters and the shapefiles


import os, fnmatch
import time

def timeconversion(time):
    hrs = int(time // 60)
    minutes = int((time % 60)//1)
    seconds = int(((time % 1)*60)//1)

    print('\nTotal Time to Complete: ' + str(hrs) + ' hours ' + str(minutes) + ' minutes ' + str(seconds) + ' seconds\n')


# ___________________________________________________ Define input/output folders ___________________________________________________

# infloder is for input raster of RAW data. That is, prior to resampling the dataset
inFolder = r'I:/ProjectName/Clipping/0_Data/'

# outfolder is for the dataset resampled to the required spatial resolution
outFolder = r'I:/ProjectName/Clipping/'

# outFolderClipped is for the dataset After clipping to the required shapefile extent
outFolderClipped = r'G:/ProjectName/Part1/0_RAW_DATA/1_input_data_resampled_clipped/'


# ___________________________________________________ Define Shapefile Directory ___________________________________________________
shape = r'I:/ProjectName/Clipping/Boundaries/Africa_Parts/Parts_Stage_2/'


# ___________________________________________________ Resampling ___________________________________________________

# os.chdir (inFolder)

# def findfileextension (path, filter):
#     for root, dirs, files in os.walk(path):
#         for file in fnmatch.filter(files, filter):
#             yield file

# for raster in findfileextension(inFolder, 'GW_sustainability_signed_16_africa.tif'):
#     inRaster = inFolder + '/' + raster
#     outRaster = outFolder + raster

# Google Earth Engine 90m scale is equal to 0.000808483755707569 in EPSG: '4326'
# #    cmd = 'gdalwarp -tr %s %s -r near -co "TFW=YES" %s %s' % ( 0.00083330961,  0.00083331318, inRaster, outRaster)
#     cmd = 'gdalwarp -tr %s %s -r near -co "TFW=YES" %s %s' % ( 0.00083330961,  0.00083331318, inRaster, outRaster)
    
#     os.system(cmd)

# ___________________________________________________ Clipping ___________________________________________________


# Pick only the required files by filtering for file extension
os.chdir (inFolder)

# File Lists
rasterfilelist = []
shapefilelist = []

def findfileextension (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file

for raster in findfileextension(inFolder, '*.tif'):
    rasterfilelist.append(raster)

for shapefilename in findfileextension(shape, '*.shp'):
    shapefilelist.append(shapefilename)


# Feedback for detected files
print('\nPicked the following .tif Files: \n')
count = 1

for file in rasterfilelist:
    print('  ' + str(count) + '. ' + file)
    count = count + 1
print('\n\n')

print('Picked the following .shp Files: \n')
count = 1

for file in shapefilelist:
    print('  ' + str(count) + '. ' + file)
    count = count + 1
print('\n\n')

total_start = time.time()

# ___________________________________________________ Clipping Iteration ___________________________________________________
for shapefile in shapefilelist:
    shp_start = time.time()
    shp_name_split = shapefile.split('_')
    
# Shape File name extraction    
    shp_index = shp_name_split[-1].split('.')[0]

# output part folder generation
    out_part_folder = outFolder + 'part_' + shp_index + '/0_Data'

    try:
        os.makedirs(out_part_folder, exist_ok = True)
        print("\nDirectory '%s' created successfully\n" % shp_index)
    except OSError as error:
        print("\nDirectory '%s' can not be created\n" % shp_index)

# Output folder and Raster Name Generation
    for image in rasterfilelist:
        image_start = time.time()
        print('Current Shapefile: ' + shapefile)
        print('Current Raster: ' + image + '\n')

        shapename = shape + shapefile
        inRaster = inFolder + image
        outRaster = out_part_folder + '/clipped_' + shp_index + '_' + image
        
        print('Current Output Folder: ' + out_part_folder)
        print('Current Shapefile: ' + shapename)
        print('Current Input Raster: ' + inRaster)
        print('Current Output Raster: ' + outRaster + '\n')

# Clipping the Raster
        cmd = 'gdalwarp -q -cutline %s -crop_to_cutline %s %s' % (shapename, inRaster, outRaster)
        os.system(cmd)

        image_end = time.time()
        elapsed_time = image_end - image_start
        timeconversion(elapsed_time)
        print('Elapsed Time for the Raster: ' + str(elapsed_time/60) + ' minutes\n')
        print('__________________________________________________________________________________________________________________________________________')
    shp_end = time.time()
    shp_elapsed_time = shp_end - shp_start
    timeconversion(shp_elapsed_time)
    # print('Elapsed Time for the Shapefile ' + str(shp_index) + ': ' + str(shp_elapsed_time/60) + ' minutes')
    print('__________________________________________________________________________________________________________________________________________')

total_end = time.time()
total_elapsed_time = total_end - total_start
timeconversion(total_elapsed_time)
# print('Total Elapsed Time: ' + str(total_elapsed_time/60) + ' minutes')
print('__________________________________________________________________________________________________________________________________________')