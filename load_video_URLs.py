

def load_urls(filename):
    urls=[]
    with open(filename, 'r') as fl:
        urls = [url.strip() for url in fl]
    print(urls)
    return urls




