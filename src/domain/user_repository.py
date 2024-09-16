from abc import ABC, abstractmethod

from domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User): ...

    @abstractmethod
    def get_user(self, id: int) -> User | None: ...

    @abstractmethod
    def delete_user(self, id: int) -> None: ...
