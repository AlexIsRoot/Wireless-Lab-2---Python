import math
import statistics

# Extracting data from the file containing the output of the iperf server
def extract_data(log_file):
    data = []
    with open(log_file, 'r') as file:
        for line in file:
            if line.startswith("[  5]  ") :
                data.append(float(line.split("  ")[5].strip().split(' ')[0]))

    return data

def calculate_mean(data):
    return statistics.mean(data)

def calculate_std_dev(data, mean):
    return statistics.stdev(data)

# Removing each 12th element to remove per-round bitrate mean
def remove_every_12th_element(array):
    return [array[i] for i in range(len(array)) if (i + 1) % 12 != 0]

def main():

    #input file
    input_file=input("Filename: ")

    data = extract_data(input_file)
    data = remove_every_12th_element(data)
    mean = calculate_mean(data)
    std_dev = calculate_std_dev(data, mean)

    # Appending computed values in the original file
    with open(input_file, 'a') as file:
        file.write("Mean: " + str(round(mean, 2)) + " Mbits/sec\n")
        file.write("Standard Deviation: " + str(round(std_dev, 2)) + " Mbits/sec\n")
        file.write("Minimum: " + str(min(data)) + " Mbits/sec")
        file.write("\nMaximum: " + str(max(data)) + " Mbits/sec")


if __name__ == "__main__":
    main()
