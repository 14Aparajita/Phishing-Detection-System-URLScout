import re
from urllib.parse import urlparse
import math
from collections import Counter

# First Directory Length
def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def digit_count(url):
    return sum(c.isdigit() for c in url)

def letter_count(url):
    return sum(c.isalpha() for c in url)

def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

# Use of IP or not in domain
def having_ip_address(url):
    match = re.search(
        # IPv4 in hexadecimal
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'  
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # IPv6
    if match:
        return -1
    else:
        return 1

def hostname_length(url):
    return len(urlparse(url).netloc)

def url_length(url):
    return len(urlparse(url).path)

def subdomain_count(url):
    netloc = urlparse(url).netloc
    return netloc.count('.') - 1  # Subdomains are separated by dots

def entropy(url):
    url = urlparse(url).netloc + urlparse(url).path
    counts = Counter(url)
    total_chars = len(url)
    return -sum((count / total_chars) * math.log2(count / total_chars) for count in counts.values())

def digit_proportion(url):
    url_length = len(url)
    digit_count = sum(c.isdigit() for c in url)
    return digit_count / url_length if url_length > 0 else 0

def suspicious_keyword(url):
    suspicious_keywords = ['login', 'secure', 'verify', 'account']
    return any(keyword in url for keyword in suspicious_keywords)

# Gets all count features
def get_counts(url):
    count_features = []

    count_features.append(url.count('-'))
    count_features.append(url.count('@'))
    count_features.append(url.count('?'))
    count_features.append(url.count('%'))
    count_features.append(url.count('.'))
    count_features.append(url.count('='))
    count_features.append(url.count('http'))
    count_features.append(url.count('https'))
    count_features.append(url.count('www'))

    return count_features
