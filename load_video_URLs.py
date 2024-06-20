
## This function is to load urls in videos_url.txt into list
##Param : {filename} is the name of the file which is video_urls.txt
# Returns list of urls
def load_urls(filename):
    urls=[]
    with open(filename, 'r') as fl:
        urls = [url.strip() for url in fl]
    print(urls)
    return urls




