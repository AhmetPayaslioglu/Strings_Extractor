import re

def extract_strings(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    strings = re.findall(b'[\x20-\x7E]{10,}', data)
    urls = re.findall(b'https?://[a-zA-Z0-9\./-]+', data)
    return [string.decode() for string in strings], [url.decode() for url in urls]

strings, urls = extract_strings('file.bin')

with open('output.txt', 'w') as f:
    for string in strings:
        f.write(string + '\n')
    for url in urls:
        f.write(url + '\n')

