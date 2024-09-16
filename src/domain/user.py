from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(init=True, kw_only=True, order=True)
class User:
    __id: UUID = field(default_factory=uuid4)

    def __init__(self, id: UUID | str, name: str, email: str):
        if isinstance(id, str):
            id = UUID(id)
        self.__id = id
        self.__name = name
        self.__email = email

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
