import json




def get_price_score(data):
    return data['data'][0]['price_score']


def get_galaxy_score(data):
    return data['data'][0]['galaxy_score']


def get_rank(data):
    return data['data'][0]['alt_rank']
