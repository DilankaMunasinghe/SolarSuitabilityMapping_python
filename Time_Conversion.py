def timeconversion(time):
    hrs = int(time // 60)
    minutes = int((time % 60)//1)
    seconds = int(((time % 1)*60)//1)

    print('\nTotal Time to Complete: ' + str(hrs) + ' hours ' + str(minutes) + ' minutes ' + str(seconds) + ' seconds\n')

timeconversion(231.79938238859177)