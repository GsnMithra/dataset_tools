import os

path = '/Volumes/Expansion/Deep Learning/dataset_tools/data_set/images/train'
images = os.listdir (path)

seen = dict ()
for image in images:

    if image[:2] == '._': continue

    res = ''.join([char for char in image if not char.isdigit()]) 
    res = res[0:-4]

    if res in seen: seen[res] += 1
    else: seen[res] = 1

sorted_set = dict (sorted (seen.items (), key = lambda x: x[1]))
weak_data = list ()

max_value = 0
items = 0

for K, V in sorted_set.items ():
    if V < 800: weak_data.append (K)
    max_value += V
    items += 1
    print (f'{K}: {V}')

print (f'total dataset size: {max_value}')
print (f'weak datasets: {weak_data}')
print (f'mean of the dataset size: {int (max_value / items)}')
