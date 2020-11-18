import re
import requests


pattern = r'<a[^>]*?href=[\"|\'](?:.+://)*([\w|.|-]+\w)'

url = 'http://pastebin.com/raw/7543p0ns'
res = requests.get(url).text
with open('urls.txt', 'w') as text:
    text.write(res)
result = re.findall(pattern, res)
result = set(result)
result = list(result)
result.sort()

print(*result, sep='\n')
