import re
import sys
import argparse
import requests
from urllib.parse import urlparse, parse_qs

def extract_query_params(js_code):
    found_params = set()
    query_matches = re.findall(r'[\?&]([a-zA-Z0-9_]+)=', js_code)
    found_params.update(query_matches)
    return found_params

def extract_object_params(js_code):
    found_params = set()

    object_matches = re.findall(r'(?:params|data)\s*:\s*{([^}]+)}', js_code)
    for obj in object_matches:
        keys = re.findall(r'["\']?([a-zA-Z0-9_]+)["\']?\s*:', obj)
        found_params.update(keys)

    stringify_matches = re.findall(r'JSON\.stringify\s*\(\s*{([^}]+)}\s*\)', js_code)
    for obj in stringify_matches:
        keys = re.findall(r'["\']?([a-zA-Z0-9_]+)["\']?\s*:', obj)
        found_params.update(keys)

    return found_params

def is_valid_param(param):
    return not param.isdigit() and len(param) > 1

def extract_params_from_script(js_code):
    query_params = extract_query_params(js_code)
    object_params = extract_object_params(js_code)
    combined = query_params.union(object_params)
    filtered = [param for param in combined if is_valid_param(param)]
    return sorted(filtered)

def process_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        js_code = response.text
        return extract_params_from_script(js_code)
    except:
        return []

def main():
    parser = argparse.ArgumentParser(description="Extract parameters from JS URLs")
    parser.add_argument('-i', '--input', required=True, help="Input file with JS URLs")
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except:
        sys.exit(1)

    all_params = set()
    for url in urls:
        params = process_url(url)
        all_params.update(params)

    for param in sorted(all_params):
        print(param)

if __name__ == "__main__":
    main()
