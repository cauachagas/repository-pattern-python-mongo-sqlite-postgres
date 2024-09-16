from uuid import UUID

import domain


class CreateUser:
    def __init__(self, repository: domain.UserRepository):
        self.__repository = repository

    def execute(self, id: UUID, name: str, email: str):
        user = domain.User(id=id, name=name, email=email)
        self.__repository.add_user(user)


class GetUser:
    def __init__(self, repository: domain.UserRepository):
        self.__repository = repository

    def execute(self, id: UUID) -> domain.User | None:
        user = self.__repository.get_user(id)
        if isinstance(user, domain.User):
            return user
        return None


class DeleteUser:
    def __init__(self, repository: domain.UserRepository):
        self.__repository = repository

    def execute(self, id: UUID):
        self.__repository.delete_user(id)
