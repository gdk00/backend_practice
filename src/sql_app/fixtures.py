import factory
from sqlalchemy.orm import scoped_session

from sql_app import models
from sql_app.database import SessionLocal
from sql_app.models import Person

print("crete fixures")


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Person
        sqlalchemy_session = scoped_session(SessionLocal)
        sqlalchemy_get_or_create = ('email',)

    id = 1
    email = "root@root.com"
    hashed_password = "1234"

print(scoped_session(SessionLocal).query(Person).all())

UserFactory(email='root@root.com')
user = UserFactory.create()


print(user)
# print(Person.query().all())
print(scoped_session(SessionLocal).query(Person).all())
