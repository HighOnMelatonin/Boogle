# Boogle
boogle is a discord bot that provides search results from various websites


invite link: https://discord.com/api/oauth2/authorize?client_id=914402388591394848&permissions=274877926400&scope=bot


This repository contains modules for searching Reddit, YouTube, MyAnimeList and Boogle itself. The search modules can only return the top result from the various sites at this juncture.



# How Boogle Works:

Enter query after '??' and it will return the first google result from the query

Example:

        ??python
        
        Embeded link: https://www.python.org/


Other prefixes for different searches:

        ?a: First anime result from myanimelist
        ?m: First manga result from myanimelist
        ?y: First video result from youtube
        ?r: Returns first result from reddit (sorted by relevance)
        ?r/: Returns first result from the subreddit (sorted by relevance)

Searching subreddits:

        ?r/audiophile hd600

        Embeded link: https://www.reddit.com/r/audiophile/comments/efgx4c/just_got_sennheiser_hd600s_for_christmas/

Note the space between the subreddit name and the query
