from datetime import datetime, time
def date_diff_in_Seconds(datetime2, datetime1):
  timedelta = datetime2 - datetime1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
datetime1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
datetime2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(datetime2, datetime1)) + '\n')