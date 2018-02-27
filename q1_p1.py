import datetime
import csv

converted_datetime_file = open("datetimes.txt", "w")

# Open the prices file and convert
with open('prices_sample.csv', newline='') as f:
    reader = csv.reader(f)
    # Iterate over the lines in prices_sample
    for Unix_Time in reader:
        # Write the converted unix_time to datetime to datetimes.txt file
        converted_datetime_file.write("%s\n" %
                datetime.datetime.fromtimestamp(
                int(Unix_Time[0])
            ).strftime('%Y-%m-%d %H:%M:%S'))

# Close the file once write has completed
converted_datetime_file.close()