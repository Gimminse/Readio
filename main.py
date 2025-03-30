import yt_dlp
from abc import ABC, abstractmethod
import schedule
import time
import requests

class SummarizerBase(ABC):
    @abstractmethod
    def download(self):
        raise NotImplementedError

    @abstractmethod
    def transcribe(self, path):
        raise NotImplementedError

    @abstractmethod
    def summarize(self, transcript):
        raise NotImplementedError

class LiveSummarizer(SummarizerBase):
    def __init__(self):
        self.url = None
        self._summary = None
        self._subscription = []
        self._stream_info = {}
    
    @property
    def getUrl(self):
        return self.url
    
    @property
    def getSummary(self):
        return self._summary
    
    @property
    def getSubscription(self):
        return self._subscription
    
    @property
    def getStreaminfo(self):
        return self._stream_info
    
    def setUrl(self, url):
        self.url = url

    def setSummary(self, summary):
        self._summary = summary
    
    def addSubscription(self, channel):
        self._subscription.append(channel)
    
    def setStreaminfo(self, info):
        self._stream_info = info

    def download(self):
        """
            Return: path
        """
        url = self.getUrl
        ydl_opts = {'quiet': True, 'skip_download': True, 'format': 'bestaudio'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            d = ydl.extract_info(url, download=False)
            self.setStreaminfo(d)
            return d['path']



    def transcribe(self, path):
        transcript = 0
        self.transcript = transcript
        return 1

    def summarize(self, transcript):
        summary = 0
        self.summary = summary
        return 1
    
    @property
    def program(self):
        path = self.download()
        self.transcribe(path)
        self.summarize()
        self.free()
    
    def free(self):
        self.url = None
        self._summary = None
        self._subscription = None
        self._stream_info = None
    

def main():
    pass

    

if __name__=='__main__':
    main()

