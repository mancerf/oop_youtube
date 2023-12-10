import os
import json
from googleapiclient.discovery import build



class Channel:
    """Класс для ютубчик-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UCwHL6WHUarjGfUM_586me8w'


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.channel['items'][0]['statistics']['videoCount']

    @classmethod
    def get_service(cls):
        '''возращает объект длы работы с YouTube API'''
        return cls.youtube

    def to_json(self, document):
        '''сохраняющий в файл значения атрибутов экземпляра Channel'''
        with open(document, 'w', encoding= 'utf8') as file:
            json.dump(
                {
                    'channel_id': self.__channel_id,
                    'title': self.title,
                    'description': self.description,
                    'video_count': self.video_count,
                    'url': self.url,
                    'subscriberCount': self.subscriberCount,
                    'videoCount': self.view_count
                }, file,indent=2, ensure_ascii=False)







    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

