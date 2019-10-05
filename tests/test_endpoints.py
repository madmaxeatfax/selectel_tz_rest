import pytest
import sys

sys.path.append("..")
from joke_api import app, db
from joke_api.models import User, Joke


@pytest.fixture
def client():
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.create_all()

    yield app.test_client()

    db.drop_all()


def test_jokes_random(client):
    url = "/api/v1/jokes/random"
    login, user_id = "FinnTheHuman", 1
    users_table = db.session.query(User)
    testcase_num = 5

    for i in range(testcase_num):
        res = client\
            .get(url + "?login=%s" % login)\
            .json

        assert res["user_id"] == user_id,\
            "wrong user get a joke"

        assert res["joke"]["id"] == i+1,\
            "joke have wrong id"

        assert res["joke"]["content"] == res["joke"]["content"].strip(),\
            "joke have trailing whitespaces"

    user = users_table.filter(User.login == login).first()
    assert len(user.jokes) == testcase_num,\
        "sent != recieved"


def test_jokes(client):
    url = "/api/v1/jokes"
    login, user_id = "JakeTheDog", 1
    users_table = db.session.query(User)

    cases = [
        "I own the world's worst thesaurus. Not only is it awful, it's awful.",
        "Parenthood is feeding the mouth that bites you.",
        "Artificial intelligence is no match for natural stupidity.",
        "Filthy, stinking rich; well, two out of three ain't bad."
    ]

    # TEST POST
    for j in cases:
        res = client.post(
            url+"?login=%s" % login,
            data={"joke": j}
        ).json

        assert "user" in res and "joke" in res\
            and "id" in res["user"]\
            and "login" in res["user"]\
            and "id" in res["joke"]\
            and "content" in res["joke"],\
            "[POST] responce schema is invalid"

        assert res["user"]["id"] == user_id,\
            "[POST] wrong user get a joke"

    user = users_table.filter(User.login == login).first()
    assert [j.content for j in user.jokes] == cases,\
        "[POST] sent != recieved"

    # TEST GET
    res = client.get(url+"?login=%s" % login).json

    assert [j["content"] for j in res["jokes"]] == cases,\
        "[GET] wrong collection of jokes returned"

    assert res["user"]["id"] == user_id and res["user"]["login"] == login,\
        "[GET] wrong user returned"
