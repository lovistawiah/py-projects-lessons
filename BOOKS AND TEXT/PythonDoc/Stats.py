import statistics
#this module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mea = statistics.mean(data)
print(mea)

media = statistics.median(data)
print(media)

varian = statistics.variance(data)
print(varian)