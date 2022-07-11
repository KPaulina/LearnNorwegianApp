import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user_test(db) -> User:
    return User.objects.create_superuser(username="admin")


def test_user_created(user_test: User) -> None:
    assert user_test.username == 'admin'
    assert user_test.is_superuser

