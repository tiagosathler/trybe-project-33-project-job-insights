from src.counter import count_ocurrences
from unittest.mock import mock_open, patch
from pytest import fixture


@fixture
def mock_file_data():
    return (
        "python javascript react Python JavaScript PYTHON JAVASCRIPT"
    )


def test_counter(mock_file_data):
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        assert count_ocurrences("dummy", "python") == 3
