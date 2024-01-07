from requests import get


'''
search only returns the video id, in the form of /watch?v=<id>"
'''
def search(term, num_results=10, lang="en", proxy=None):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = f"https://www.youtube.com/results?search_query={escaped_search_term}"

        proxies = None
        if proxy:
            if proxy[:5]=="https":
                proxies = {"https":proxy}
            else:
                proxies = {"http":proxy}

        response = get(google_url, headers=usr_agent, proxies=proxies)    
        response.raise_for_status()

        return response.text

    html = fetch_results(term, num_results, lang)

    #Get the video ID
    idStart = html.find('{"url":"/watch')
    idEnd = html[idStart:].find(',"webPageType"')

    vidId = html[idStart + 8:idStart + idEnd - 1]

    #Get the title of the video
    titleStart = html.find('"title":{"runs":[{"text":')
    titleEnd = html[titleStart:].find('}],"accessibility":{')
    vidTitle = html[titleStart + 26: titleStart + titleEnd - 1]

    vidTitle = vidTitle.replace('\\','')

    return vidId,vidTitle    
