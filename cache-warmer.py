import subprocess
import concurrent.futures
import argparse

# Fastly Cache Warmer
#
# Usage:
# python3 cache-warmer.py --file="url-list.txt" --target="https://google.com/" --threads=10

# Default values for command-line arguments
default_url_list_file = "url-list-example.txt"
default_base_url = "https://google.com/"
default_max_threads = 10

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process URLs from a URL list file.")
parser.add_argument("--file", type=str, default=default_url_list_file, help="Text file containing URLs")
parser.add_argument("--target", type=str, default=default_base_url, help="Base URL to target")
parser.add_argument("--threads", type=int, default=default_max_threads, help="Number of concurrent threads")
args = parser.parse_args()

if not args.file or not args.target or args.threads is None:
    parser.print_usage()
    exit(1)

base_url = args.target
url_list_file = args.file
max_threads = args.threads

def execute_curl(url, count, total):
    print(f'({count}/{total}) Processing URL: {base_url}{url}', end='', flush=True)
    curl_command = f'curl --silent {base_url}{url} -o /dev/null -H "Connection: close" -H "Fastly-Debug:1"'

    try:
        subprocess.check_output(curl_command, shell=True, text=True)
        print(f' - OK', end='\n')
    except subprocess.CalledProcessError as e:
        print(f' - FAILED', end='\n')
        print(e)

def process_urls(url_list):
    total_items = len(url_list)
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = []
        for count, url in enumerate(url_list, start=1):
            futures.append(executor.submit(execute_curl, url, count, total_items))
        for future in concurrent.futures.as_completed(futures):
            pass

if __name__ == "__main__":
    with open(url_list_file, 'r') as file:
        url_list = [line.strip() for line in file.readlines() if line.strip()]
        process_urls(url_list)

    print("Done.")
