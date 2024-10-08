import sys
import os
import time

def clean_pcap(argv):
    hashes = []
    inbase = os.getcwd() + '/'
    outbase = os.getcwd() + '/'

    for file in os.listdir(inbase):
        if os.path.isfile(inbase + file):  # Check if it is a file
            print(file)
            inputfile = inbase + file
            outputfile = outbase + file
            print("Creating temp file")
            command1 = 'tcprewrite --dlt=enet --infile=' + inputfile + ' --outfile=temp.pcap'
            print("Step 1 done")
            time.sleep(.03)
            command2 = 'tcprewrite --enet-dmac=11:11:11:11:11:11 --enet-smac=11:11:11:11:11:11 --pnat=192.168.0.0/16:1.1.1.1/32 --infile=temp.pcap --outfile=' + outputfile
            print("Step 2 done")
            time.sleep(.03)

            os.system(command1)
            os.system(command2)
            return outbase

