import os
import cleaner, split, nim_hash, makehash

# Step 1: Clean the PCAP file using cleaner.py
path_cleaned_data = cleaner.clean_pcap('b1.pcap')

# Step 2: Split the cleaned data for processing using split.py
split.split(path_cleaned_data)  # Now passes the file path correctly

# Step 3: Hash the strings using makehash.py, return path to the files
makehash.hashes('/home/kali/Desktop/sensor-detection-paper/code/smart_reckon/hash_code/captures/1-minute')

# Step 4: Perform machine learning to identify IoT devices using nim_hash.py
nim_hash.nim('/home/kali/Desktop/sensor-detection-paper/code/smart_reckon/hash_code/1-minute-hashes-cleaned.csv')
