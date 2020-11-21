import hashlib


def encrypt(str):
    return hashlib.sha256(str.encode()).hexdigest()


def toList(source):
    list = []
    for item in source:
        list.extend(item)

    return list

