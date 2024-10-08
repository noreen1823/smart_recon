import os
import cleaner, split, nim_hash, makehash

# Get the base directory of the current script file
base_dir = os.path.dirname(os.path.abspath(__file__))

# Step 1: Clean the PCAP file using cleaner.py
pcap_file_path = os.path.join(base_dir, 'captures', 'b1.pcap')
path_cleaned_data = cleaner.clean_pcap(pcap_file_path)

# Step 2: Split the cleaned data for processing using split.py
split.split(path_cleaned_data)

# Step 3: Hash the strings using makehash.py, return path to the files
hash_input_path = os.path.join(base_dir, 'captures', '1-minute')
makehash.hashes(hash_input_path)

# Step 4: Perform machine learning to identify IoT devices using nim_hash.py
hash_csv_path = os.path.join(base_dir, 'hash_code', '1-minute-hashes-cleaned.csv')
nim_hash.nim(hash_csv_path)
