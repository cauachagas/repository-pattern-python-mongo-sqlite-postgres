import interfaces_adapters


def Mongo():
    uri = "mongodb://root:example@localhost:27017/"
    db_name = "repository"
    return interfaces_adapters.UserMongoDBRepository(uri, db_name)


def SQLite():
    uri = "db.sqlite3"
    return interfaces_adapters.UserSQLiteRepository(uri)


def Postgre():
    DATABASE_URL = "postgresql://app_user:app_password@localhost:5432/postgres"
    # DATABASE_URL = (
    #     "user=app_user password=app_password host=localhost dbname=postgres port=5432"
    # )
    return interfaces_adapters.UserPostgreRepository(DATABASE_URL)


class UserDB(enumerate):
    MONGO = Mongo()
    SQLITE = SQLite()
    POSTGRE = Postgre()
