import os
import subprocess

def splitter(input_pcap, outputbase, increment):
    command = "tshark -r " + input_pcap + " -T fields -e frame.time_relative"
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    splitted = out.split(b"\n")
    if len(splitted) < 2:
        print(f"Error processing {input_pcap}: insufficient data")
        return

    last_second = int(float(splitted[-2]))
    window_insecond = 60 * 1

    counter = 1
    if last_second > window_insecond:
        for i in range(0, last_second, 60 * 1):
            start_time = i
            end_time = i + window_insecond
            output_pcap = os.path.join(outputbase, f"{os.path.basename(input_pcap).split('.')[0]}-{counter}.pcap")

            command = (
                f"tshark -r {input_pcap} -Y 'frame.time_relative >= {start_time} "
                f"and frame.time_relative <= {end_time}' -w {output_pcap}"
            )
            os.system(command)

            if (end_time + 60 * 1) > last_second:
                break
            counter += 1

    print("Finished processing", input_pcap)

def split(path):
    if os.path.isfile(path) and path.endswith(".pcap"):
        input_pcap = path
        outputbase = os.path.dirname(path)  # Use the same directory as the input file
        splitter(input_pcap, outputbase, 1)
    elif os.path.isdir(path):
        for folder in os.listdir(path):
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.endswith(".pcap"):  # Only process .pcap files
                        input_pcap = os.path.join(folder_path, file)
                        print(folder_path)
                        outputbase = os.path.join(folder_path, '1-minute/')
                        os.makedirs(outputbase, exist_ok=True)
                        splitter(input_pcap, outputbase, 1)
    else:
        raise ValueError("Provided path is neither a valid pcap file nor a directory.")
