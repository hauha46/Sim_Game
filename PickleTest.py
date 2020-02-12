import pickle
config_dictionary = {'remote_hostname': 'google.com', 'remote_port': 80}
abc = {1:'2', 3:'4'}
# Step 2
with open('config.dictionary', 'wb') as config_dictionary_file:
    # Step 3
    pickle.dump(config_dictionary, config_dictionary_file)
with open('config.dictionary', 'wb') as config_dictionary_file:
    # Step 3
    pickle.dump(abc, config_dictionary_file)

temp = 0
with open('config.dictionary', 'rb') as config_dictionary_file:
    # Step 3
    temp = pickle.load(config_dictionary_file)

    # After config_dictionary is read from file
    print(temp)