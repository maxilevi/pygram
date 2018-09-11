from InstagramAPI import InstagramAPI
import scheduler


class Instagrammer:

    def __init__(self, config: dict):
        self.config = config
        self.instagram_api = InstagramAPI(self.config['username'], self.config['password'])
        self.schedule_items = scheduler.load()
        self.tags = self.config['tags']

    def start(self):
        if len(self.schedule_items) == 0:
            raise ValueError("There are no scheduled images.")
        self.instagram_api.login()
        upload_item_key = list(self.schedule_items.keys())[0]
        self.upload(self.schedule_items[upload_item_key])
        del self.schedule_items[upload_item_key]
        scheduler.save(self.schedule_items)

    def upload(self, upload_options: dict):
        caption = Instagrammer.create_caption(upload_options, self.tags, self.config)
        print(f"Uploading image with caption:\n{caption}")
        self.instagram_api.uploadPhoto(upload_options['image'], caption=caption)

    @staticmethod
    def create_caption(upload_options: dict, tags: list, config: dict):
        return f"{upload_options['caption']}\n{config['extra_caption']}\n.\n.\n{(' #'.join(upload_options['tags'] + tags)).strip()}"
