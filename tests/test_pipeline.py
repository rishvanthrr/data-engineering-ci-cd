from unittest.mock import Mock


def test_mock_data_source():
    mock_source = Mock()

    mock_source.get_data.return_value = [10, 20, 30]

    data = mock_source.get_data()

    assert data == [10, 20, 30]


def test_number_of_rows():
    data = pd.DataFrame({
        "name": ["Arun", "Priya", "Rahul"],
        "age": [25, 30, 28],
        "salary": [30000, 40000, 35000]
    })

    result = transform_data(data)

    assert len(result) == 3


def test_columns_exist():
    data = pd.DataFrame({
        "name": ["Arun"],
        "age": [25],
        "salary": [30000]
    })

    result = transform_data(data)

    assert "name" in result.columns
    assert "age" in result.columns
    assert "salary" in result.columns





import pandas as pd
from src.pipeline import transform_data


def test_salary_transformation():
    data = pd.DataFrame({
        "name": ["Arun", "Priya"],
        "age": [25, 30],
        "salary": [30000, 40000]
    })

    result = transform_data(data)

    assert result["salary"].tolist() == [33000, 44000]