from fastapi import APIRouter
from config import settings

class Routering(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = settings.api_prefix.v1
        self.tags = ["API V1"]

