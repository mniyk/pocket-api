"""pocket.pyのunittest
"""
import configparser
import logging
import unittest

from pocket import Pocket


logging.basicConfig(
    level=logging.INFO,
    format='\t'.join([
        '%(asctime)s',
        '%(levelname)s',
        '%(filename)s',
        '%(funcName)s',
        '%(processName)s',
        '%(process)d',
        '%(threadName)s',
        '%(thread)d',
        '%(message)s']))
logger = logging.Logger(__name__)


class TestPocket(unittest.TestCase):
    def setUp(self) -> None:
        config = configparser.ConfigParser()
        config.read('settings.ini')

        self.api = Pocket(
            consumer_key=config.get('POCKET', 'CONSUMER_KEY'),
            access_token=config.get('POCKET', 'ACCESS_TOKEN'))

    def test_get_list(self) -> None:
        self.api.get_list()

        print(self.api.pockets)

    def test_get_tags(self) -> None:
        self.api.get_list()
        self.api.get_tags()

        print(self.api.tags)
