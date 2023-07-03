import argparse
import requests

def check_url(url):
    response = requests.head(url)
    return response.status_code == 200

def generate_urls(base_url, words):
    urls = []
    for word in words:
        url = f"{base_url}/{word}"
        urls.append(url)
    return urls

# Parse command-line arguments
parser = argparse.ArgumentParser(description='URL Generation and Validation')
parser.add_argument('-u', '--url', required=True, help='Base URL')
parser.add_argument('-w', '--wordlist', required=True, help='Word list file')
args = parser.parse_args()

base_url = args.url
word_list_file = args.wordlist

# Read words from the specified file
with open(word_list_file, "r") as file:
    word_list = [word.strip() for word in file.readlines()]

urls = generate_urls(base_url, word_list)
for url in urls:
    if check_url(url):
        print(f"{url} is a valid URL.")
    else:
        print(f"{url} is an invalid URL.")
