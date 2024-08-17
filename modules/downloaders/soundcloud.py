from sclib import SoundcloudAPI, Track
from .shcemas import MediaDownloaded
from .base import BaseDownloader


class SoundCloud(BaseDownloader):
    
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.soundcloud_client = SoundcloudAPI()
        
        
    def download_music(self) -> MediaDownloaded:
        """download_misic method for download soundcloud music

        Returns:
            str: music path
        """
                
        try:
            
            music = self.soundcloud_client.resolve(self.url)
            
            filename = rf'{self.save_music_path}/{music.title}.mp3'

            with open(filename, 'wb+') as file:
                music.write_mp3_to(file)
                
            media = MediaDownloaded(PATH=filename, TITLE=music.title, CAPTION=music.description)

        except Exception as e:
            print("Error in SoundCloud - download_music method :", e)
            media = MediaDownloaded()
        
        return media