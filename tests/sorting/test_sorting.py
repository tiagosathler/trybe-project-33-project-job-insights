from src.sorting import sort_by
import pytest


@pytest.fixture
def mock_jobs():
    return [
        {"min_salary": 1000, "max_salary": 25000, "date_posted": "2018-05-05"},
        {"min_salary": 500, "max_salary": 20000, "date_posted": "2019-05-05"},
        {"min_salary": 2000, "max_salary": 30000, "date_posted": "2021-05-05"},
        {"max_salary": 15000, "date_posted": "2015-05-05"},
        {"min_salary": 3000, "date_posted": "2014-05-05"},
        {"min_salary": 4000, "max_salary": 14000},
    ]


def test_sort_by_criteria(mock_jobs):
    expected = {
        "min_salary": [
            {
                "min_salary": 500,
                "max_salary": 20000,
                "date_posted": "2019-05-05",
            },
            {
                "min_salary": 1000,
                "max_salary": 25000,
                "date_posted": "2018-05-05",
            },
            {
                "min_salary": 2000,
                "max_salary": 30000,
                "date_posted": "2021-05-05",
            },
            {"min_salary": 3000, "date_posted": "2014-05-05"},
            {"min_salary": 4000, "max_salary": 14000},
            {"max_salary": 15000, "date_posted": "2015-05-05"},
        ],
        "max_salary": [
            {
                "min_salary": 2000,
                "max_salary": 30000,
                "date_posted": "2021-05-05",
            },
            {
                "min_salary": 1000,
                "max_salary": 25000,
                "date_posted": "2018-05-05",
            },
            {
                "min_salary": 500,
                "max_salary": 20000,
                "date_posted": "2019-05-05",
            },
            {"max_salary": 15000, "date_posted": "2015-05-05"},
            {"min_salary": 4000, "max_salary": 14000},
            {"min_salary": 3000, "date_posted": "2014-05-05"},
        ],
        "date_posted": [
            {
                "min_salary": 2000,
                "max_salary": 30000,
                "date_posted": "2021-05-05",
            },
            {
                "min_salary": 500,
                "max_salary": 20000,
                "date_posted": "2019-05-05",
            },
            {
                "min_salary": 1000,
                "max_salary": 25000,
                "date_posted": "2018-05-05",
            },
            {"max_salary": 15000, "date_posted": "2015-05-05"},
            {"min_salary": 3000, "date_posted": "2014-05-05"},
            {"min_salary": 4000, "max_salary": 14000},
        ],
    }

    for criteria in ["max_salary", "min_salary", "date_posted"]:
        test_subject = list(mock_jobs)
        sort_by(test_subject, criteria)
        assert all(
            [
                expected[criteria][i] == test_subject[i]
                for i in range(len(expected[criteria]))
            ]
        )


def test_sort_by_value_error(mock_jobs):
    test_subject = list(mock_jobs)
    try:
        sort_by(test_subject, "xablau")
    except ValueError:
        with pytest.raises(ValueError, match="invalid sorting criteria: x"):
            sort_by(test_subject, "x")
    else:
        assert False
