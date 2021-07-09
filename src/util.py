import requests
import discord
import io,os,json
import random
from dotenv import load_dotenv


hold_url = [
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


def get_coinInfo(coin):
    url='https://api.lunarcrush.com/v2?'
    payload={'data':'assets', 'key':os.getenv('LUNAR_TOKEN'), 'symbol': coin.upper(), 'data_points' :'0'}
    response = requests.get(url , params=payload)
    json_data = json.loads(response.text)
    print(response.url)
    return json_data
