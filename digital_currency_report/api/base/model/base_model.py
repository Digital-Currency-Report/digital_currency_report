from pydantic import BaseModel as Model

from digital_currency_report.common.json import loads, dumps


class BaseModel(Model):
    class Config:
        json_loads: loads
        json_dumps: dumps
