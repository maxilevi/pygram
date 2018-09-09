from InstagramAPI import InstagramAPI
import schedule


class Instagrammer:

    def __init__(self, config: dict):
        self.instagram_api = InstagramAPI(config['username'], config['password'])
        self.schedule_items = schedule.load()

    def start(self):
        self.instagram_api.login()
        upload_item_key = list(self.schedule_items.keys())[0]
        self.upload(self.schedule_items[upload_item_key])
        del self.schedule_items[upload_item_key]
        schedule.save(self.schedule_items)

    def upload(self, upload_options: dict):
        self.instagram_api.uploadPhoto(upload_options['image'], caption=Instagrammer.create_caption(upload_options))

    @staticmethod
    def create_caption(upload_options: dict):
        return f"{upload_options['caption']}\n.\n.#{' #'.join(upload_options['tags'])}"
