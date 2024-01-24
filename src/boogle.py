import discord
from gsearch.googlesearch import search as gsearch
import random
from youtubesearch.youtubesearch import search as ytsearch
from myanimelist import manga
from myanimelist import anime
from reddit import redditsearch
from reddit import subsearch

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
# Need to enable messages in intent to see message content

with open('.env', 'r') as file:
    lines = file.readlines()
    TOKEN = lines[0]


messages = ['I found this', 'This is what I could find','Here you go','','Hope this helps']
greetings = ['hello', 'hi','hey','yo','sup']
prefixes = ['??','?a','?m','?y']


def googlesearch(query):
    responses = gsearch(query, num_results = 1)
    results = []
    results.extend(responses)
    return results[0]


@client.event
async def on_ready():
    ##Output guilds to console, to indicate bot is live
    guilds = []
    for guild in client.guilds:
        guilds += [guild]

    print(f'{client.user} is connected to the following guild:')
    for guild in guilds:
        print(f'{guild.name:<25} {str(guild.id):^35}')


def sendHelp():
    ##Help message
    help_title = 'How I work:'

    pythonlink = googlesearch('python')
    audiolink = subsearch.search('audiophile','hd600')

    helpmessage = f'''Enter query after \'??\' and I will return the first google result from the query
        \nExample:
        \n> ??python
        > Embeded link: {pythonlink}
        \n\nOther prefixes for different searches:
        ```
    ?a: First anime result from myanimelist
    ?m: First manga result from myanimelist
    ?y: First video result from youtube
    ?r: Returns first result from reddit (sorted by relevance)
    ?r/: Returns first result from the subreddit (sorted by relevance)
        ```
        \nSearching subreddits:
        \n> ?r/audiophile hd600
        > Embeded link: {audiolink}
        \nNote the space between the subreddit name and the query
        '''

    return help_title, helpmessage


def getresponse(prefix, query):
    ##Get a response based on query
    if prefix == '??':
        response = gsearch(query)

    elif prefix == '?a':
        response = anime.search(query)

    elif prefix == '?m':
        response = manga.search(query)

    elif prefix == '?y':
        vidId,query = ytsearch(query)
        response = f"https://www.youtube.com{vidId}"

    elif prefix == '?r':

        ##If there's a '/' search the subreddit
        if query[0] == '/':
            query = query[1:]
            space = query.find(' ')
            subreddit = query[:space]
            terms = query[space + 1:]
            response = subsearch.search(subreddit, terms)

        else:
            response = redditsearch.search(query)

    else:
        return None

    return response


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@914402388591394848>'):
        ##If boogle is pinged, send help
        if 'thank' in message.content.lower():
            await message.channel.send("My pleasure :)")
        title, helpmessage = sendHelp()
        await message.channel.send(embed = discord.Embed(title = title, description = helpmessage))
        return

    query = message.content[2:]
    prefix = message.content[0:2]

    try:
        if query[0] == '?':
            return

    except IndexError:
        return

    if prefix in prefixes:
        if query == 'h' or query == 'help':
            title, helpmessage = sendHelp()
            await message.channel.send(embed = discord.Embed(title = title, description = helpmessage))
            return

        elif query.lower() in greetings:
            greeting = random.choice(greetings)
            await message.channel.send(greeting)
            return

        elif 'thank' in query.lower():
            await message.channel.send("My pleasure :)")
            return

    response = getresponse(prefix, query)

    if response:
        embeded = discord.Embed(title = query, url = response)
        rmessage = random.choice(messages)
        await message.channel.send(content = rmessage, embed = embeded)
        return

    else:
        return


##Suggestion: might want to add a feature that records all the times boogle was unintentionally called "shut up boogle", "go away boogle"

client.run(TOKEN)
