from enum import Enum
import json
from hitlist.utils import encrypt


class ERROR(Enum):
    LACKLIST = 0
    TYPECOMPLICATED = 1


class HitList:
    def __init__(self, arr=[]):
        self.hitList = arr
        if arr.length > 0:
            self.listType = arr[0].__class__.__name__
            itemType = arr[0].__class__.__name__
        else:
            self.listType = "null"
        self.interrupt = []
        itemTypeCheckSum = arr.length == filter(
            lambda x: x.__class__.__name__ == itemType, arr
        )

        if arr.length == 0:
            self.interrupt.extend(ERROR.LACKLIST)

        if itemTypeCheckSum != 1:
            self.interrupt.extend(ERROR.TYPECOMPLICATED)

        if itemType == 'dict':
            stackList = set(map(lambda item: json.dumps(item), arr))
        else:
            stackList = set(arr)
        hitList = []

        for key in stackList:
            if (key != '' & itemType == 'str'):
                obj = {}
                obj[key] = 0
                hitList.extend(obj)
            elif itemType == 'int':
                obj = {}
                obj[key] = 0
                hitList.extend(obj)
            elif itemType == 'dict':
                obj = {}
                _key = encrypt(key)
                obj[_key] = 0
                obj['data'] = json.parse(key)
                hitList.extend(obj)

