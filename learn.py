Machine learning

#MEAN MEDIAN MODE
"""
MEAN untuk mencari nilai rata-rata
MEDIAN untuk mencari nilai tengah
MODE untuk mencari nilai yang sering muncul
"""

import numpy
from scipy import stats
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.mean(speed)
print (x) #89.76923076923077

x = numpy.median(speed)
print (x) #87.0

x = stats.mode(speed)
print (x) #ModeResult(mode=array([86]), count=array([3]))

#STANDARD DEVIATION
"""
Data = [32, 111, 138, 28, 59, 77, 97]
VARIANCE(s^2)
1. Find the mean
77.4

2. For each value, find the difference from the mean
32 - 77.4 = -45.4
111 - 77.4 = 33.6
138 - 77.4 = 60.6
28 - 77.4 = -49.4
59 - 77.4 = -18.4
77 - 77.4 = -0.4
97 - 77.4 = 19.6

3. For each difference, find the square value
(-45.4)^2 = 2061.16
(33.6)^2 = 1128.96
(60.6)^2 = 3672.36
(-49.4)^2 = 2440.36
(-18.4)^2 = 38.56
(-0.4)^2 = 0.16
(19.6)^2 = 384.16

4. Variance adalah rata-rata dari hasil no. 3
(2061.16 + 1128.96 + 3672.36 + 2440.36 + 38.56 + 0.16 + 384.16) / 7 = 1432.2

STANDARD DEVIATION/ SIMPANGAN BAKU (s)
Akar pangkat 2 dari VARIANCE
V1432.2 = 37.85
"""
import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print (x) #1432.2448979591834

import numpy
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.std(speed)
print (x) #37.84501153334721

#PERCENTILE
"""
Membagi data menjadi 100 bagian
Data = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

1. Urutkan data
[2, 5, 6, 7, 8, 11, 15, 25, 27, 31, 31, 32, 36, 39, 41, 43, 48, 50, 61, 80, 82]

2. Percentile ke 75
(75 * (banyak_data + 1)) / 100
= (75 * (21 + 1)) / 100
= 16.5 (Data ke-16)

3. Data ke 16 + 0.5 (Data ke 17 - Data ke 16)
= 43 + 0.5 (48 - 43)
= 45.5

Namun di NumPy hanya sampai di langkah ke 2 (data ke-roundown)
"""

import numpy
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(ages, 75)
print (x) #43

#DATA DISTRIBUTION
"""
Membuat 250 random float antara 0.0 - 5.0
"""
import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print (x)

"""
Membuat histogram
"""
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform (0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

#NORMAL DATA DISTRIBUTION
"""
Atau disebut Gaussian data distribution / bell curve
"""
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal (5.0, 1.0, 100000) #mean = 5.0 std = 1.0 values = 100000
plt.hist(x, 100)
plt.show()
