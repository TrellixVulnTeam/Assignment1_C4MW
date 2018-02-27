import datetime
import csv

def median(prices):
    prices = sorted(prices)
    length = len(prices)
    if length % 2 != 0:
        return prices[int((len(prices) - 1) / 2)]
    else:
        return (prices[int(len(prices) / 2)] + prices[int((len(prices) / 2) - 1)]) / 2

def standardev(prices, mean):
    count = 0
    sumsq = 0
    for i in prices:
        sumsq = sumsq + (i - mean)** 2
        count = count + 1
    return (sumsq / count) **(1/2.0)


price_list = []
time = []

# Open the prices file and convert
with open('prices_sample.csv', newline='') as f:
    reader = csv.reader(f)
    # Iterate over the lines
    for row in reader:
        time.append(row[0])
        price_list.append(float(row[1]))

max_price = max(price_list)
min_price = min(price_list)
# Find the time at which the max and min price was reached
for i in range(0, 150000):
    if price_list[i] == min_price:
        # Index where min time was reached
        min_index = i
    if price_list[i] == max_price:
        # Index where max time was reached
        max_index = i

# print("Max: ", max(price_list))
# print("Min: ", min(price_list))
# print ("Mean", (sum(price_list)/float(len(price_list))))

print("Min price achieved at time: ",datetime.datetime.fromtimestamp(
                int(time[min_index])
            ).strftime('%Y-%m-%d %H:%M:%S'))
print("Max price achieved at time: ",datetime.datetime.fromtimestamp(
                int(time[max_index])
            ).strftime('%Y-%m-%d %H:%M:%S'))
print("Median: ", median(price_list))
print("Standard Deviation: ", standardev(price_list, (sum(price_list)/float(len(price_list)))))