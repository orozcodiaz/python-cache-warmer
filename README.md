# Fastly Cache Warmer

This Python script is designed to warm up the cache on Fastly Content Delivery Network (CDN) by sending requests to a list of URLs. Warming the cache ensures that your content is readily available to users and can help improve website performance. Usually used after the deployment process.

## Prerequisites

Before using this script, make sure you have the following installed:

- Python 3.x
- The `curl` command-line tool (used for sending HTTP requests)

## Usage

To use the script, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone git@github.com:orozcodiaz/python-cache-warmer.git
   ```

   or

   ```shell
   git clone https://github.com/orozcodiaz/python-cache-warmer.git
   ```

2. Enter the folder:

   ```shell
   cd python-cache-warmer/
   ```

3. Modify `url-list.txt` and run the code (don't forget to modify the target parameter):

   ```shell
   python3 cache-warmer.py --file="url-list.txt" --target="https://google.com/" --threads=10
   ```

