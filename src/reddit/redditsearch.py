from requests import get

def search(query):
    '''
    Returns the top result from a reddit search
    '''

    def fetch_result(query):
        reddit_url = f"https://www.reddit.com/search/?q={query}"
        response = get(reddit_url)

        return response.text

    html = fetch_result(query)

    ##Get link
    start = html.find('class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"')
    end = html[start:].find('<div class="_2SdHzo12ISmrC8H86TgSCp _1zpZYP8cFNLfLDexPY65Y7 "')

    sublink = html[start + 60: start + end - 2]
    link = f"https://www.reddit.com{sublink}"

    return link
