from app.handlers.base import HandlerBase
import json


class PublicAccount(HandlerBase):
    def get(self, *args, **kwargs):
        self.write("hello world")

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        print("data:", data)
        self.write(data)
