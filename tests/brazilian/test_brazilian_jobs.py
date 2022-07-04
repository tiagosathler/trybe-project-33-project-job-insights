from inspect import trace
from src.brazilian_jobs import read_brazilian_file
from unittest.mock import mock_open, patch
from pytest import fixture


@fixture
def mock_file_data():
    return "titulo,salario,tipo\n" "Maquinista,2000,trainee"


def test_brazilian_jobs(mock_file_data):
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        expected = [
            {"title": "Maquinista", "salary": "2000", "type": "trainee"}
        ]
        assert read_brazilian_file("dummy")[0] == expected[0]
