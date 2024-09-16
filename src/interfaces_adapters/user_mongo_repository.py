from uuid import UUID

from pymongo import MongoClient

from domain.user import User
from domain.user_repository import UserRepository


class UserMongoDBRepository(UserRepository):
    def __init__(self, uri: str, db_name: str):
        self.__db = MongoClient(uri, uuidRepresentation="standard")[db_name]
        self.__collection = self.__db.get_collection("users")

    def add_user(self, user: User):
        data = {"_id": user.id, "name": user.name, "email": user.email}
        self.__collection.insert_one(data)

    def get_user(self, id: UUID) -> User | None:
        data = self.__collection.find_one({"_id": id})
        if isinstance(data, dict):
            data["id"] = data["_id"]
            del data["_id"]
            return User(**data)
        return None

    def delete_user(self, id: UUID):
        self.__collection.delete_one({"_id": id})
