"""Pocketを操作するためのモジュール
"""
import requests


class Pocket:
    def __init__(self, consumer_key: str, access_token: str) -> None:
        """初期化

        Args:
            consumer_key (str): Web APIのコンシュマーキー
            access_token (str): Web APIのアクセストークン

        Examples:
            >>> api = Pocket(
                    access_token=config.get('POCKET', 'CONSUMER_KEY'),
                    access_token=config.get('POCKET', 'ACCESS_TOKEN'))
        """
        self.consumer_key = consumer_key
        self.access_token = access_token
        self.pockets = None
        self.tags = None

    def get_list(self):
        """リストの取得

        Examples:
            >>> api.get_list()
        """
        url = 'https://getpocket.com/v3/get'

        self.pockets = []

        params = {
            'consumer_key': self.consumer_key,
            'access_token': self.access_token,
            'detailType': 'complete'}

        response = requests.get(url, params=params)

        json_data = response.json()

        for k, v in json_data['list'].items():
            tags = list(v['tags'].keys()) if 'tags' in v else []

            self.pockets.append({
                'key': k, 
                'title': v['given_title'], 
                'url': v['given_url'], 
                'tags': tags})

    def get_tags(self):
        """タグのリストを取得

        Examples:
            >>> api.get_tags()
        """
        tags = []

        for p in self.pockets:
            tags.extend(p['tags'])

        self.tags = set(tags)
