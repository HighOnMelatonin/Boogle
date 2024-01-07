from requests import get

def search(subreddit, query):
    '''
    Returns the top result from a subreddit search
    Parameter subreddit should be just the name of the subreddit, 'r/memes' should be passed in as 'memes'
    '''

    def fetch_result(subreddit, query):
        subreddit_url = f"https://www.reddit.com/r/{subreddit}/search/?q={query}&restrict_sr=1&sr_nsfw="
        response = get(subreddit_url)

        return response.text

    html = fetch_result(subreddit, query)

    chunkStart = html.find("<post-consume-tracker>")
    chunkEnd = html.find("</post-consume-tracker>")
    chunk = html[chunkStart:chunkEnd]
    # cut the html file down to a smaller chunk

    ##Get link
    start = chunk.find(f'href="/r/{subreddit}/comment')
    end = chunk[start:].find('class="absolute inset-0"')

    sublink = chunk[start + 6: start + end - 5]
    # substring found is 'href="/r/{subreddit}/comments/{someURL}"'
    link = f"https://www.reddit.com{sublink[:-2]}"
    # the -2 index is required cuz for some reason sublink keeps returning with an ending "


    return link
