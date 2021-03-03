#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, FLOAT
from sqlalchemy.dialects.postgresql import TIME

from digital_currency_report.common.database.base import base
from digital_currency_report.database.models.mixins import ChangeMixin, EnableMixin, UuidMixin


class PoolDB(base, UuidMixin, ChangeMixin, EnableMixin):
    __tablename__ = "pool"
    # 子账号用户名
    username: Column = Column(String(48), nullable=False)
    # 虚拟币类型
    coin: Column = Column(String(32), nullable=False)
    # 观察者hash
    url_hash: Column = Column(String(32))
    # 结算单位
    unit: Column = Column(String(16), nullable=False)
    # 哈希率
    cur_hashrate: Column = Column(FLOAT, nullable=False)
    # 每日结算时间
    time: Column = Column(TIME)

if __name__ == '__main__':
    pass
