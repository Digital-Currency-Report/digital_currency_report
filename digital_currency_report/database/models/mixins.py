from sqlalchemy import Integer, Boolean, Column, func

from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP


class IdMixin:
    id = Column(Integer, nullable=False, primary_key=True)


class AutoIdMixin:
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)


class UuidMixin:
    uuid = Column(UUID(as_uuid=True), nullable=False, primary_key=True)


class CreatedMixin:
    created = Column(TIMESTAMP, nullable=False, default=func.now())


class ModMixin:
    last_modified = Column(TIMESTAMP, nullable=False, default=func.now(), onupdate=func.now())


class ChangeMixin(CreatedMixin, ModMixin):
    pass


class EnableMixin:
    enable = Column(Boolean, nullable=True, default=True)
