from typing import List, Dict, Union
import json


def get_db(file: str = "data.json") -> List[Dict[str, Union[str, int]]]:
    with open(file, encoding="utf-8") as file:
        db = json.load(file)
    return db


def save_db(db, file: str = "data.json") -> None:
    with open(file, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)


def get_db_users(file: str = "users.json") -> List[Dict[str, Union[str, int]]]:
    with open(file, encoding="utf-8") as file:
        db = json.load(file)
    return db

def save_db_users(db, file: str = "users.json") -> None:
    with open(file, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)
