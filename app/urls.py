from app.handlers.login import LoginHandler, QRHandler
import os

urls = [(r"/login/", LoginHandler), (r"/qr/", QRHandler)]
