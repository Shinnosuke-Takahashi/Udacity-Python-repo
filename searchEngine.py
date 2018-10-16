#THIS CODE IS CURRENTLY UNDER DEVELOPMENT AND IS UPDATED REGULARLY.
# This is a search engine under development.
# THE FOLLOWING IS A LOG OF UPDATES:
# 10-9-18: defined crawl_web()
# 10-8-18: improved get_all_links() by calling newly defined function union()
# 10-2-18: defined get_all_links()
# 9-28-18: start date; defined get_next_target()

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
    return crawled
