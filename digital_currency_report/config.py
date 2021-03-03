#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

from pydantic import BaseSettings

from digital_currency_report.common.json import dumps


class Config(BaseSettings):
    DEBUG: bool = True
    PROJECT_NAME: str = 'digital_currency_report'
    PROJECT_PATH: Path = Path(__file__).parent.resolve()
    RELEASE: str
    TAG: str

    # database
    DB_HOST: str = 'postgres'
    DB_PORT: int = 5432
    DB_USERNAME: str = 'postgres'
    DB_PASSWORD: str = 'postgres'
    DB_TABLE: str = 'digital_currency_report'
    # database url
    DB_URL: str
    SQLALCHEMY_URL: str

    class Config:
        json_dumps = dumps
        extra = 'allow'

    def get(self, item: str, default=None) -> Any:
        return getattr(self, item, default)

    def __setitem__(self, key: str, value: Any) -> None:
        return self.__setattr__(key, value)

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://" \
               f"{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@" \
               f"{quote_plus(self.DB_HOST)}:{quote_plus(str(self.DB_PORT))}/" \
               f"{quote_plus(str(self.DB_TABLE))}"

    @property
    def SQLALCHEMY_URL(self) -> str:
        return f"postgresql+psycopg2://" \
               f"{self.DB_USERNAME}:{self.DB_PASSWORD}@" \
               f"{self.DB_HOST}:{self.DB_PORT}/" \
               f"{self.DB_TABLE}"

    @property
    def RELEASE(self) -> str:
        release_file = self.PROJECT_PATH.parent.resolve().joinpath('RELEASE')
        if release_file.is_file():
            with open(release_file, 'r') as f:
                return f.read()
        return "1.0.0"


config = Config()
if __name__ == '__main__':
    for k, v in config.dict().items():
        print(k, v)
