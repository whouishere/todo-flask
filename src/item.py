import uuid

class Item:
    def __init__(self, text: str, is_done: bool = False):
        self.text = text
        self.is_done = is_done
        self.uuid = uuid.uuid4()

    def set_text(self, text: str):
        self.text = text

    def set_is_done(self, is_done: bool):
        self.is_done = is_done

    def get_uuid(self) -> uuid.UUID:
        return self.uuid
