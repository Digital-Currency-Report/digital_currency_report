#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, String, FLOAT
from sqlalchemy.dialects.postgresql import UUID

from digital_currency_report.common.database.base import base
from digital_currency_report.database.models.mixins import ChangeMixin, EnableMixin, AutoIdMixin
from digital_currency_report.database.models.pool import PoolDB


class CoinMinerDB(base, AutoIdMixin, ChangeMixin, EnableMixin):
    __tablename__ = "pool"
    pool_uuid: Column = Column(UUID(as_uuid=True), ForeignKey(PoolDB.uuid, ondelete="CASCADE"), nullable=False)
    # 结算单位
    unit: Column = Column(String(16), nullable=False)
    # 哈希率
    cur_hashrate: Column = Column(FLOAT, nullable=False)


if __name__ == '__main__':
    pass
