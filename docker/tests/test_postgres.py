import psycopg2
import pytest


@pytest.fixture(scope="module")
def db_connection():
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="test",
        user="test",
        password="test"
    )
    yield connection
    connection.close()


class TestPostgres:
    def test_connection(self, db_connection):
        assert db_connection is not None

    def test_simple_query(self, db_connection):
        with db_connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()
        assert result == (1,)
