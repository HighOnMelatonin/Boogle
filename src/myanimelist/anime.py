from requests import get

def search(query):
    '''
    Returns the top result of an anime search on myanimelist
    '''
    def fetch_result(query):
        mal_url = f"https://myanimelist.net/search/all?q={query}"
        response = get(mal_url)

        return response.text

    html = fetch_result(query)

    #Get link
    animeIndex = html.find('<h2 id="anime">')
    animeDiv = html[animeIndex:]

    linkStart = animeDiv.find('<div class="picSurround di-tc thumb">')
    linkEnd = animeDiv[linkStart:].find('class="hoverinfo_trigger"')
    link = animeDiv[linkStart + 51:linkEnd + linkStart - 2]

    return link

