import os

# make sure you have the total path directory
# to your dataset and uncomment the below lines. 

# path_train = '<data_set/images/train>'
# path_val = '<data_set/images/val>'

listing_train = os.listdir (path_train)
listing_val = os.listdir (path_val)

train_size = len (listing_train)
val_size = len (listing_val)
total_size = train_size + val_size

print (f'train: {train_size}')
print (f'val: {val_size}')
print (f'total size: {total_size}')
