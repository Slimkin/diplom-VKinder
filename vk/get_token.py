from urllib.parse import urlencode


def get_token_link():
    APP_ID = 7413440
    #SERV_TOKEN = '2283702f2283702f2283702f4c22f26eef222832283702f7c1b754b55746d4e2cf98de9'
    VER = 5.103

    OAUTH_URL = 'https://oauth.vk.com/authorize'
    OAUTH_PARAMS = {
        'client_id': APP_ID,
        'display': 'page',
        'scope': 'offline',
        'response_type': 'token',
        'v': VER
    }

    return ('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))
