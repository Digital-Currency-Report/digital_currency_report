#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import singledispatch
from typing import Callable, Union
from uuid import UUID

import rapidjson


@singledispatch
def dumps_default(obj):
    raise TypeError(obj)


@dumps_default.register(bytes)
def obj_to_decode(obj: bytes):
    return obj.decode('utf-8')


@dumps_default.register(set)
def obj_to_decode(obj: set):
    return list(obj)


@dumps_default.register(UUID)
def obj_to_decode(obj: UUID):
    return str(obj)


def dumps(
        obj, /,
        skipkeys: bool = False,
        ensure_ascii: bool = False,
        indent: int = None,
        default: Callable = dumps_default,
        sort_keys: bool = False,
        number_mode: int = None,
        datetime_mode: int = None,
        uuid_mode: int = None,
        allow_nan: bool = True,
        is_bytes: bool = False
) -> Union[str, bytes]:
    data = rapidjson.dumps(
        obj, skipkeys=skipkeys, ensure_ascii=ensure_ascii, indent=indent,
        default=default, sort_keys=sort_keys,
        number_mode=number_mode, datetime_mode=datetime_mode, uuid_mode=uuid_mode, allow_nan=allow_nan
    )
    return data.encode('utf-8') if is_bytes else data


loads = rapidjson.loads

if __name__ == '__main__':
    pass
