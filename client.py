'''`Myrino` is an api-based library for Rubino messengers'''

from .methods import Methods, randint
from requests import session


class BaseMethod:

    client: dict = {
        'app_name': 'Main',
        'app_version': '3.0.1',
        'lang_code': 'en',
        'package': 'app.rubino.main',
        'platform': 'Android'
    }

    def url(self) -> str:
        return f'https://rubino{randint(1, 20)}.iranlms.ir/'

    video: str = 'Video'
    picture: str = 'Picture'


class Client(BaseMethod):
    pass
