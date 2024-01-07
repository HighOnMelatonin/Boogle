from requests import get

def search(query):
    '''
    Returns the top result of a manga search on myanimelist
    '''
    def fetch_result(query):
        mal_url = f"https://myanimelist.net/search/all?q={query}&cat=all#manga"
        response = get(mal_url)

        return response.text

    html = fetch_result(query)
    
    #Get link
    mangaIndex = html.find('<h2 id="manga">')
    mangaDiv = html[mangaIndex:]
    
    linkStart = mangaDiv.find('<div class="picSurround di-tc thumb">')
    linkEnd = mangaDiv[linkStart:].find('class="hoverinfo_trigger"')
    link = mangaDiv[linkStart + 51:linkEnd + linkStart - 2]

    return link
