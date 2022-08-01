import pickle

file_to_be_updated = 'levels/level1_data'

# Read
pickle_in = open(file_to_be_updated, 'rb')
world_data = pickle.load(pickle_in)

# update elements in certain position
world_data[16][7] = 2		# blob
world_data[16][8] = 0		# no elements

# Write
pickle_out = open(file_to_be_updated, 'wb')
pickle.dump(world_data, pickle_out)
pickle_out.close()
