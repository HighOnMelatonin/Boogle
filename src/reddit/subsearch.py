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

    ##Get link
    start = html.find('class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"')
    end = html[start:].find('"><div class="_2SdHzo12ISmrC8H86TgSCp _1zpZYP8cFNLfLDexPY65Y7 "')

    sublink = html[start + 60: start + end]
    link = f"https://www.reddit.com{sublink}"

    return link

