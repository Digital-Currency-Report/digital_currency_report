#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, TEXT

from digital_currency_report.common.database.base import base
from digital_currency_report.database.models.mixins import UuidMixin, ChangeMixin, EnableMixin


class Pool_DB(base, UuidMixin, ChangeMixin, EnableMixin):
    __tablename__ = "pool"

    name: Column = Column(String(32), index=True)
    url: Column = Column(TEXT)


if __name__ == '__main__':
    pass
