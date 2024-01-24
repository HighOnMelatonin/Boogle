from requests import get

def search(term, num_results = 5, lang = "en", proxy = None):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'
    }

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = f"https://www.google.com/search?q={escaped_search_term}"

        proxies = None
        if proxy:
            if proxy[:5] == "https":
                proxies = {"https": proxy}

            else:
                proxies = {"http": proxy}

        response = get(google_url, headers = usr_agent, proxies = proxies)
        response.raise_for_status()

        return response.text

    try:
        html = fetch_results(term, num_results, lang)

    except:
        return 0

    linkstart = html.find('url?esrc=s&amp;q=&amp;rct=j&amp;sa=U&amp;') + 45
    ## + 45 to account for the "url="
    linkend = html[linkstart:].find('&amp')

    link = html[linkstart:linkstart + linkend]
    return link


