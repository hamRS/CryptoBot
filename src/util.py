import requests
import discord
import io,os,json
import random
from dotenv import load_dotenv


buy_url = [
    'https://imgflip.com/i/5fyt4l',
    'https://preview.redd.it/87cyhof5lm251.jpg?width=640&crop=smart&auto=webp&s=add32f356e84f79597307868c2bc5bfd902dfebd',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHoLwHnZqoEdZEeck_eCYM8arVjdFl5t42Vw&usqp=CAU',
    'https://i.imgflip.com/5e35np.jpg',
    'https://coinmixed.eu/wp-content/uploads/2019/07/hodl5year.png',
    'https://pbs.twimg.com/media/EvWGVIiXMAE7HIN.jpg',
    'https://i.kym-cdn.com/entries/icons/original/000/026/688/greenwojak.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYZ6pXF2E3NbJZu_WmUbDBQBBDVwgrVlMf7w&usqp=CAU'
]

sell_url = [
    'https://stockhead.com.au/wp-content/uploads/2021/06/RealEmmetKelly-1407059353216204806-0-640x360.jpg',
    'https://pics.me.me/crypto-pepe-market-50426623.png',
    'https://img-9gag-fun.9cache.com/photo/aeAVvPv_460s.jpg',
    'https://i.chzbgr.com/original/14330373/h5DE06E2B/musk-dogecoin-bitcoin-ethereum-memes-funny-memes-crypto-memes-twitter-memes-funny-tweets-twitter',
    'https://i.pinimg.com/564x/e9/43/4a/e9434ab0ed2f55a0895380dbd75c96b9.jpg',
    'https://i.ytimg.com/vi/ukCRrPk5Gto/maxresdefault.jpg'
]


buy_phrase = [
    "Go ahead, buy this thing I'll wait ",
    "What are you waiting chief",
    "Great coin, buy it!",
    "Do you want me to say this or what, BUY IT",
    "Cesar cesar"
]

sell_phrases =[
    "I don't know about this one",
    "Don't",
    "Cesar",
    "Forget about it"
]

def get_coinInfo(coin):
    url='https://api.lunarcrush.com/v2?'
    payload={'data':'assets', 'key':os.getenv('LUNAR_TOKEN'), 'symbol': coin.upper(), 'data_points' :'0'}
    response = requests.get(url , params=payload)
    json_data = json.loads(response.text)
    print(response.url)
    return json_data


def make_embed_info(data):
    social_impact = data['data'][0]['social_impact_score']
    rank = data['data'][0]['alt_rank']
    galaxy_score = data['data'][0]['galaxy_score']
    desc = get_phrase(social_impact , rank , galaxy_score)
    embed = discord.Embed(
        title = data['data'][0]['name'] + ' - ' + data['config']['symbol'],
        description = '*provided by lunarcrush*\n' + '**' + desc + '**',
        colour = 10181046
    )
    embed.set_author(name='cryptoMaster', icon_url='https://www.iconpacks.net/icons/2/free-cryptocurrency-coin-icon-2422-thumb.png')
    embed.add_field(name='Price', value= '**'+str(data['data'][0]['price'])+'**' + '$' , inline=False)
    embed.set_image(url=get_image_type(social_impact, rank, galaxy_score));
    embed.add_field(name='Change 24hs %' , value = str(data['data'][0]['percent_change_24h']) , inline=True)
    embed.add_field(name='Change 30d %' , value = data['data'][0]['percent_change_30d'] , inline=True)
    embed.add_field(name='Market Cap' , value = data['data'][0]['market_cap'])
    embed.add_field(name='Rank' , value = data['data'][0]['alt_rank'], inline= False)
    return embed


def get_phrase(social_impact , rank , galaxy_score):
    if(galaxy_score >= 60 and rank <= 20 and social_impact >= 2.0):
        return random.choice(buy_phrase)
    return random.choice(sell_phrases)


def get_image_type(social_impact , rank , galaxy_score):
    if(galaxy_score >= 60 and rank <= 20 and social_impact >= 2.0):
        return get_random_buy()
    return get_random_sell()

def get_random_buy():
    return random.choice(buy_url)

def get_random_sell():
    return random.choice(sell_url)


def error_embed():
    embed = discord.Embed(
        title = 'ERROR',
        description = "I don't support this coin at the moment",
        colour = 15158332
    )
    return embed
