import subprocess
import statistics
import time


def run_iperf_tests(server_ip, num_tests=10, interval=1):
    throughput_values = []

    for i in range(num_tests):
        print("ROUND", i+1)

        # Command can be edited in order to perform different actions when calling iperf subprocess
        command = ['iperf3', '-c', server_ip, '-i', '1']
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            output_lines = result.stdout.split('\n')
            for line in output_lines:
                print(line)
                if 'sender' in line:
                    parts = line.split()
                    if len(parts) >= 7:
                        throughput = float(parts[6])
                        throughput_values.append(throughput)

        time.sleep(interval)

    if throughput_values:
        min_throughput = min(throughput_values)
        max_throughput = max(throughput_values)
        avg_throughput = statistics.mean(throughput_values)
        std_dev_throughput = statistics.stdev(throughput_values)
        print("Performance tests results:")
        print("Minimum throughput:", min_throughput, "Mbps")
        print("Maximum throughput:", max_throughput, "Mbps")
        print("Average throughput:", round(avg_throughput, 2), "Mbps")
        print("Standard deviation of throughput:", round(std_dev_throughput, 2), "Mbps")
    else:
        print("No throughput data available.")


def main():
    server_ip = input("Server IP: ")
    run_iperf_tests(server_ip)


if __name__ == "__main__":
    main()

