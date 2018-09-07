from InstagramAPI import InstagramAPI


class Grammer:

    def __init__(self, config: dict):
        self.InstagramAPI = InstagramAPI(config['username'], config['password'])
        self.candidates = self.load_candidates()

    def upload(self, path: str):
        self.InstagramAPI.uploadPhoto(path, caption='')

    def start(self):
        self.InstagramAPI.login()

    def load_candidates(self) -> list:
        candidates = []
        return candidates
