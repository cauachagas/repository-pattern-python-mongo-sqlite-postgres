from uuid import UUID, uuid4

import pytest

import use_cases
from domain.user import User
from frameworks_drivers.user_repository import UserDB


def test_domain_create_user_without_id():
    name, email = "John Doe", "john@example.com"
    user = User(id=id, name=name, email=email)
    assert user.name == name
    assert user.email == email


def test_domain_create_user_with_id():
    id, name, email = uuid4(), "John Doe", "john@example.com"
    user = User(id=id, name=name, email=email)
    assert user.id == id
    assert user.name == name
    assert user.email == email


def test_domain_create_user_with_id_str():
    id, name, email = str(uuid4()), "John Doe", "john@example.com"
    user = User(id=id, name=name, email=email)
    assert user.id == UUID(id)
    assert str(user.id) == id
    assert user.name == name
    assert user.email == email


@pytest.mark.parametrize(
    "repository",
    [
        (UserDB.MONGO),
        (UserDB.SQLITE),
        (UserDB.POSTGRE),
    ],
)
def test_user_use_case(repository):
    id, name, email = uuid4(), "John Doe", "john@example.com"
    create_user = use_cases.CreateUser(repository=repository)
    create_user.execute(id=id, name=name, email=email)

    get_user = use_cases.GetUser(repository=repository)
    user = get_user.execute(id)
    assert isinstance(user, User)
    assert user.id == id
    assert user.name == name
    assert user.email == email
    delete_user = use_cases.DeleteUser(repository=repository)
    delete_user.execute(id)
    user = get_user.execute(id)
    assert user is None
