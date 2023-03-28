import re

log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as f:
        total_response_time = 0
        num_requests = 0
        for line in f:
            match = re.search(r'\d+ ms', line)
            if match:
                response_time = int(match.group(0).split()[0])
                total_response_time += response_time
                num_requests += 1

        if num_requests == 0:
            print("No requests found in log file.")
        else:
            avg_response_time = total_response_time / num_requests
            print(f"Average response time: {avg_response_time} ms")

except FileNotFoundError:
    print(f"Error: {log_file} not found.")
