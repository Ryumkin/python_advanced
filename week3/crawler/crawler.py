import json


def get_url(json_object, url, urls):
    for i, v in json_object.items():
        new_url = url
        if new_url:
            new_url += "/"
        new_url += i
        if not v:
            urls.append(new_url)
        else:
            get_url(json_object[i], new_url, urls)


with open(input()) as reader:
    json_items = json.loads(reader.readline())
    urls = []
    get_url(json_items, "", urls)
    print(*sorted(urls), sep="\n", end="")

"""
import json


in_filename = input()
with open(in_filename, 'r') as f:
    web_index = json.load(f)

web_pages = []
stack = [
    (site_domain, section)
    for site_domain, section in web_index.items()
]

while stack:
    site_domain, section = stack.pop()
    if section:
        for a, b in section.items():
            stack.append((f'{site_domain}/{a}', b))
    else:
        web_pages.append(site_domain)

print(*sorted(web_pages), sep='\n')
"""
