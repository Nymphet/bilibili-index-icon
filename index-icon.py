# -*- coding: utf-8 -*-

import json
import gzip
import os

from urllib import request


def download_json(url):
    r = request.Request(url)
    r.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    with request.urlopen(r) as f:
        with open('index-icon.json', 'wb') as s:
            gzip_f = gzip.GzipFile(fileobj=f)
            content = gzip_f.read()
            s.write(content)


def download_gif(title, url):
    r = request.Request(url)
    r.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    with request.urlopen(r) as f:
        with open('./index-icon/%s.gif' % title, 'wb') as s:
            s.write(f.read())


def main():
    url = 'http://www.bilibili.com/index/index-icon.json'
    download_json(url)
    if not os.path.exists('index-icon'):
        os.mkdir('index-icon')
    with open('index-icon.json', 'r') as js:
        j = json.loads(js.read())
        for fix in j['fix']:
            title, url = fix['title'], fix['icon']
            print('downloading {} from {}'.format(title, url))
            download_gif(title, url)


if __name__ == '__main__':
    main()
