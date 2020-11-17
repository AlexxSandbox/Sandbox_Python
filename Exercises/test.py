import re

pattern = r'a[abc]c'
template = 'acc'

match_object = re.match(pattern, template)
print(match_object)

template = 'abc, acc, aac, dda'
all = re.findall(pattern, template)
print(all)

fix = re.sub(pattern, 'abc', template)
print(fix)
