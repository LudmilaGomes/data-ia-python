from math import sqrt
from math import log10

def form(one_freq):
    result = 80/((sqrt(1 + pow( (400/one_freq), 2))) * (sqrt(1 + pow( (one_freq/400000), 2))))
    return result

freq = [10, 100, 200, 500, 1000, 10000, 100000, 1000000, 2000000, 10000000]

my_list = []
for one_freq in freq:
    my_list.append(form(one_freq))

final = []
for one_result in my_list:
    final.append( 20*(log10(one_result)) )

print(my_list)
print(final)