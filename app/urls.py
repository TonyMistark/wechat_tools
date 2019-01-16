from app.handlers.login import LoginHandler, QRHandler
from app.handlers.public_account_im import PublicAccount
import os

urls = [(r"/login/", LoginHandler), (r"/qr/", QRHandler), (r"/public_account/im/", PublicAccount)]
