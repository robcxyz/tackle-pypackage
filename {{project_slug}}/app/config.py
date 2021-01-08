from pydantic import BaseSettings


class Config(BaseSettings):

    environment: str = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
