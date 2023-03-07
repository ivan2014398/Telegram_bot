from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    api_key: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


setting = Settings()
