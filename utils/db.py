import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_HOST: str = os.environ['MONGO_HOST']
    MONGO_USER: str = os.environ['MONGO_USER']
    MONGO_PASS: str = os.environ['MONGO_PASS']
    MONGO_DB: str = os.environ['MONGO_DB']
    MONGO_EXTRA: str = "?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    @property
    def mongo_dns(self):
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:27017/{self.MONGO_DB}{self.MONGO_EXTRA}"
