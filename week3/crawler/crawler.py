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
