def timeconversion(time):
    hrs = int(time // 60)
    minutes = int((time % 60)//1)
    seconds = int(((time % 1)*60)//1)

    print('\nTotal Time to Complete: ' + str(hrs) + ' hours ' + str(minutes) + ' minutes ' + str(seconds) + ' seconds\n')

# Opening a file
file1 = open(r'I:/Solar_Suitability_Mapping_v1_3_09_2022/Clipping/PythonScript/Read_log_text_file.py', 'r')

count = 0
check_string = 'Elapsed Time for the Raster'
raster_total_time = 0
  
while True:
    # Get next line from file
    line = file1.readline()

    if (check_string in line):
        count += 1
        time = float(line.split(' ')[5])
        raster_total_time = raster_total_time + time
  
    # if line is empty
    # end of file is reached
    if (line == 'End of File'):
        break

hrs = int(raster_total_time // 60)
minutes = int((raster_total_time % 60)//1)
seconds = int(((raster_total_time % 1)*60)//1)

timeconversion()

# print('\nTime: ' + str(hrs) + ' hours ' + str(minutes) + ' minutes ' + str(seconds) + ' seconds and ' + str(count) + ' Total Rasters Clipped\n')
file1.close()