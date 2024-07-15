#!/usr/bin/env python3
import argparse
import webbrowser
import urllib.parse

urls = [
    'https://www.hobbiesville.com/search.php?search_query={}',
    'https://acgamesonline.crystalcommerce.com/products/search?q={}',
    'https://store.401games.ca/pages/search-results?q={}',
    'https://bananagames.ca/search?q={}',
    'https://www.animealley.ca/search?type=product&options%5Bprefix%5D=last&q={}'
]

def __process_url(url_base, search):
    url = url_base.format(urllib.parse.quote(search, safe=''))

    webbrowser.open_new_tab(url)

def main(search):
    for url in urls:
        __process_url(url, search)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('search for a card in various downtown TO card stores')
    # do it like this so we can take "professor turo" and professor turo as arguments and it still works
    parser.add_argument('-s', '--search', nargs='+')
    args = parser.parse_args()

    search = ' '.join(args.search)

    main(search)