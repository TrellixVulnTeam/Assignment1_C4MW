import csv

def pearson_correlation(time_list, prices_list):
    # Local variables
    time_sum = 0
    time_sum_squared = 0
    price_sum = 0
    price_sum_squared = 0
    multiplied_sum = 0

    if len(time_list) == len(price_list):
        for i in range(0, len(price_list)):
            multiplied_sum = multiplied_sum + time_list[i] * price_list[i]

    # Sum all elements in time list
    for sum1 in time_list:
        time_sum = time_sum + sum1

    # Sum all elements in prices list
    for sum2 in prices_list:
        price_sum = price_sum + sum2

    sum_x_y_over_n = (time_sum * price_sum) / len(price_list)

    numerator = multiplied_sum - sum_x_y_over_n

    # Sum all squared elements in time list
    for sum1 in time_list:
        time_sum_squared = time_sum_squared + sum1**2

    # Sum all squared elements in prices list
    for sum2 in prices_list:
        price_sum_squared = price_sum_squared + sum2**2

    denominator = (time_sum_squared - ((time_sum ** 2)/len(time_list))) * (price_sum_squared - ((price_sum ** 2)/len(price_list)))

    return numerator/(denominator ** (1/2.0))


file_path = input("Please enter file name: ")

# Local variables
price_list = []
time = []

# Open the file specified by the user and convert
with open(file_path, newline='') as f:
    reader = csv.reader(f)
    # Iterate over the lines
    for row in reader:
        # Append the two columns into two lists for pearson correlation
        time.append(float(row[0]))
        price_list.append(float(row[1]))

print ("Pearson Correlation: ", pearson_correlation(time, price_list))
